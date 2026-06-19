import argparse
import json
from dataclasses import dataclass

@dataclass
class VPSInstance:
    name: str
    ip: str
    port: int

def deploy_vps(name: str, ip: str, port: int) -> VPSInstance:
    """ Deploy a VPS instance.
    
    Args:
    - name (str): The name of the VPS instance.
    - ip (str): The IP address of the VPS instance.
    - port (int): The port number of the VPS instance.
    
    Returns:
    - VPSInstance: The deployed VPS instance.
    """
    if port < 0 or port > 65535:
        raise ValueError("Invalid port number")
    
    # Simulate deployment process
    print(f"Deploying VPS instance {name} at {ip}:{port}...")
    return VPSInstance(name, ip, port)

def main():
    parser = argparse.ArgumentParser(description="Automated VPS deployment script")
    parser.add_argument("--name", required=True, help="Name of the VPS instance")
    parser.add_argument("--ip", required=True, help="IP address of the VPS instance")
    parser.add_argument("--port", required=True, type=int, help="Port number of the VPS instance")
    args = parser.parse_args()
    try:
        vps_instance = deploy_vps(args.name, args.ip, args.port)
        print(f"VPS instance {vps_instance.name} deployed successfully at {vps_instance.ip}:{vps_instance.port}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
