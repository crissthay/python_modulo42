import json
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional, Any


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=3, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def load_json(path: str) -> list[dict[str, Any]]:
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: '{path}' not found")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in '{path}' - {e}")
        return []


def main() -> None:
    records = load_json("space_stations.json") + load_json(
        "invalid_stations.json"
    )
    print("Space Station Data Validation")
    for record in records:
        try:
            station = SpaceStation.model_validate(record)
            print("=" * 50)
            print("Valid station created:")
            print(f"ID: {station.station_id}")
            print(f"Name: {station.name}")
            print(f"Crew: {station.crew_size} people")
            print(f"Power:z {station.power_level}%")
            print(f"Oxygen: {station.oxygen_level}%")
            print(
                f"Status: "
                f"{'Operational' if station.is_operational else 'Offline'}"
            )
            print()
        except ValidationError as e:
            print("=" * 50)
            print("Expected validation error:")
            print(e.errors()[0]["n"])
            print()


if __name__ == '__main__':
    main()