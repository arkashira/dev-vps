import datetime
import smtplib
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

@dataclass
class Metric:
    timestamp: datetime.datetime
    cpu: float
    memory: float

@dataclass
class DevBox:
    owner_email: str
    metrics: List[Metric] = field(default_factory=list)
    last_alert_time: Optional[datetime.datetime] = None

class DevBoxMonitor:
    """
    Monitor DevBoxes for CPU/Memory usage, trigger alerts, and retain metrics.
    """
    def __init__(self, retention_days: int = 30):
        self.devboxes: Dict[str, DevBox] = {}
        self.retention = datetime.timedelta(days=retention_days)

    def register_devbox(self, devbox_id: str, owner_email: str) -> None:
        if devbox_id in self.devboxes:
            raise ValueError(f"DevBox {devbox_id} already registered")
        self.devboxes[devbox_id] = DevBox(owner_email=owner_email)

    def collect_metrics(
        self,
        devbox_id: str,
        cpu: float,
        memory: float,
        timestamp: Optional[datetime.datetime] = None
    ) -> None:
        if devbox_id not in self.devboxes:
            raise ValueError(f"DevBox {devbox_id} not registered")
        ts = timestamp or datetime.datetime.utcnow()
        metric = Metric(timestamp=ts, cpu=cpu, memory=memory)
        self.devboxes[devbox_id].metrics.append(metric)

    def check_alerts(self) -> None:
        """
        Check each devbox for sustained CPU >80% over 2 minutes.
        Sends an email alert if condition met.
        """
        now = datetime.datetime.utcnow()
        for devbox_id, devbox in self.devboxes.items():
            # Sort metrics by timestamp
            metrics = sorted(devbox.metrics, key=lambda m: m.timestamp)
            streak_start = None
            streak_count = 0
            for metric in metrics:
                if metric.cpu > 80.0:
                    if streak_start is None:
                        streak_start = metric.timestamp
                        streak_count = 1
                    else:
                        # Ensure metrics are within 10s intervals
                        if (metric.timestamp - metrics[metrics.index(metric)-1].timestamp).total_seconds() <= 10:
                            streak_count += 1
                        else:
                            streak_start = metric.timestamp
                            streak_count = 1
                else:
                    streak_start = None
                    streak_count = 0

                if streak_count >= 12:  # 12 samples * 10s = 120s
                    # Check if we already alerted for this period
                    if devbox.last_alert_time is None or streak_start > devbox.last_alert_time:
                        subject = f"CPU Alert for DevBox {devbox_id}"
                        body = (
                            f"CPU usage exceeded 80% for more than 2 minutes on DevBox {devbox_id}.\n"
                            f"Start time: {streak_start.isoformat()}\n"
                            f"Current time: {now.isoformat()}"
                        )
                        send_email(devbox.owner_email, subject, body)
                        devbox.last_alert_time = now
                    break  # Only one alert per check

    def cleanup_old_metrics(self) -> None:
        """
        Remove metrics older than retention period.
        """
        cutoff = datetime.datetime.utcnow() - self.retention
        for devbox in self.devboxes.values():
            devbox.metrics = [m for m in devbox.metrics if m.timestamp >= cutoff]

def send_email(to_address: str, subject: str, body: str) -> None:
    """
    Send an email via local SMTP server.
    """
    msg = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP("localhost") as server:
        server.sendmail("monitor@devbox.com", to_address, msg)
