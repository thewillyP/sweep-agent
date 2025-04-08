# dto.py
import json
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class SweepDTO:
    sweep_id: str
    program: str
    name: str
    config: Dict[str, Any]

    def to_json(self) -> str:
        return json.dumps({
            "sweep_id": self.sweep_id,
            "program": self.program,
            "name": self.name,
            "config": self.config
        })

    @classmethod
    def from_json(cls, json_str: str) -> 'SweepDTO':
        data = json.loads(json_str)
        return cls(
            sweep_id=data["sweep_id"],
            program=data["program"],
            name=data["name"],
            config=data["config"]
        )