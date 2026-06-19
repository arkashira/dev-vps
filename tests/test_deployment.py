from deployment import deploy_vps, VPSInstance

def test_deploy_vps():
    name = "test-vps"
    ip = "192.168.1.100"
    port = 8080
    vps_instance = deploy_vps(name, ip, port)
    assert isinstance(vps_instance, VPSInstance)
    assert vps_instance.name == name
    assert vps_instance.ip == ip
    assert vps_instance.port == port

def test_deploy_vps_invalid_port():
    name = "test-vps"
    ip = "192.168.1.100"
    port = -1
    try:
        deploy_vps(name, ip, port)
        assert False, "Expected ValueError to be raised"
    except ValueError:
        assert True

def test_main():
    # Test main function with valid arguments
    import sys
    import io
    from unittest.mock import patch
    with patch("sys.argv", ["deployment.py", "--name", "test-vps", "--ip", "192.168.1.100", "--port", "8080"]):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            from deployment import main
            main()
            assert "VPS instance test-vps deployed successfully at 192.168.1.100:8080" in fake_stdout.getvalue()

    # Test main function with invalid arguments
    with patch("sys.argv", ["deployment.py"]):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
                from deployment import main
                try:
                    main()
                except SystemExit:
                    assert "error: the following arguments are required: --name, --ip, --port" in fake_stderr.getvalue()
