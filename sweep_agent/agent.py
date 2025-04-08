import argparse
import requests
import subprocess
import json
import sys

def get_sweep(server_url, sweep_id):
    response = requests.get(f"{server_url}/get_sweep/{sweep_id}")
    if response.status_code == 200:
        data = response.json()
        return data['config']
    elif response.status_code == 404:
        print("No sweeps left")
        return None
    else:
        print(f"Error: {response.json()['message']}")
        return None

def run_sweep(config):
    program = config['program']
    # Pass the config as a JSON string via command-line argument
    config_json = json.dumps(config)
    subprocess.run(['python', program, '--config', config_json])

def main():
    parser = argparse.ArgumentParser(description='Sweep Agent')
    parser.add_argument('sweep_id', help='Sweep ID')
    parser.add_argument('server_url', help='Server URL')
    args = parser.parse_args()

    config = get_sweep(args.server_url, args.sweep_id)
    if config:
        run_sweep(config)

# Library function to access config (for use in main.py)
def get_config():
    parser = argparse.ArgumentParser(description='Sweep Config Parser')
    parser.add_argument('--config', type=str, help='JSON config string')
    args, unknown = parser.parse_known_args()  # Parse only known args, ignore others
    if args.config:
        return json.loads(args.config)
    return None

if __name__ == '__main__':
    main()