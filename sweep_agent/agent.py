import argparse
import requests
import subprocess
import json
import sys
from dto import SweepDTO

def get_sweep(server_url, sweep_id):
    response = requests.get(f"{server_url}/get_sweep/{sweep_id}")
    if response.status_code == 200:
        data = response.json()
        return SweepDTO(
            sweep_id=data['sweep_id'],
            program=data['program'],
            name=data['name'],
            config=data['config']
        )
    elif response.status_code == 404:
        print("No sweeps left")
        return None
    else:
        print(f"Error: {response.json()['message']}")
        return None

def run_sweep(dto: SweepDTO):
    # Pass the DTO as a JSON string via command-line argument
    dto_json = dto.to_json()
    subprocess.run(['python', dto.program, '--dto', dto_json])

def main():
    parser = argparse.ArgumentParser(description='Sweep Agent')
    parser.add_argument('sweep_id', help='Sweep ID')
    parser.add_argument('server_url', help='Server URL')
    args = parser.parse_args()

    dto = get_sweep(args.server_url, args.sweep_id)
    if dto:
        run_sweep(dto)

def get_sweep_config() -> SweepDTO | None:
    parser = argparse.ArgumentParser(description='Sweep Config Parser')
    parser.add_argument('--dto', type=str, help='JSON DTO string')
    args, unknown = parser.parse_known_args()
    if args.dto:
        return SweepDTO.from_json(args.dto)
    return None

if __name__ == '__main__':
    main()