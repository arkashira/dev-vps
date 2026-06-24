import datetime
from unittest.mock import patch, MagicMock

import pytest

from devbox_monitor import DevBoxMonitor, send_email

@pytest.fixture
def monitor():
    m = DevBoxMonitor(retention_days=30)
    m.register_devbox("devbox-1", "owner@example.com")
    return m

def test_collect_metrics_stores_data(monitor):
    ts = datetime.datetime.utcnow()
    monitor.collect_metrics("devbox-1", cpu=50.0, memory=1024.0, timestamp=ts)
    devbox = monitor.devboxes["devbox-1"]
    assert len(devbox.metrics) == 1
    metric = devbox.metrics[0]
    assert metric.timestamp == ts
    assert metric.cpu == 50.0
    assert metric.memory == 1024.0

def test_alert_triggered_on_sustained_high_cpu(monitor):
    # Simulate 13 high CPU samples over 130 seconds
    base_ts = datetime.datetime.utcnow()
    for i in range(13):
        ts = base_ts + datetime.timedelta(seconds=10 * i)
        monitor.collect_metrics("devbox-1", cpu=85.0, memory=2048.0, timestamp=ts)

    with patch("devbox_monitor.send_email") as mock_send:
        monitor.check_alerts()
        mock_send.assert_called_once()
        args, kwargs = mock_send.call_args
        assert args[0] == "owner@example.com"
        assert "CPU Alert" in args[1]
        assert "devbox-1" in args[2]

def test_no_alert_for_short_spike(monitor):
    # Simulate 5 high CPU samples over 50 seconds
    base_ts = datetime.datetime.utcnow()
    for i in range(5):
        ts = base_ts + datetime.timedelta(seconds=10 * i)
        monitor.collect_metrics("devbox-1", cpu=90.0, memory=2048.0, timestamp=ts)

    with patch("devbox_monitor.send_email") as mock_send:
        monitor.check_alerts()
        mock_send.assert_not_called()

def test_cleanup_removes_old_metrics(monitor):
    # Add one old metric and one recent metric
    old_ts = datetime.datetime.utcnow() - datetime.timedelta(days=31)
    recent_ts = datetime.datetime.utcnow()
    monitor.collect_metrics("devbox-1", cpu=30.0, memory=512.0, timestamp=old_ts)
    monitor.collect_metrics("devbox-1", cpu=40.0, memory=512.0, timestamp=recent_ts)

    monitor.cleanup_old_metrics()
    devbox = monitor.devboxes["devbox-1"]
    assert len(devbox.metrics) == 1
    assert devbox.metrics[0].timestamp == recent_ts
