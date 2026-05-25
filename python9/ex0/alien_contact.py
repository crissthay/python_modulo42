from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=3, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("OMEGAVERSE")
    print("=" * 30)
    validate_stations = SpaceStation(
        station_id="ISS001",
        name="Omega TaeRae",
        crew_size=20,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True,
        notes="ALIEN KIM TAERAE"
    )
    
    print("Valid station created:")
    print("ID:", validate_stations.station_id)
    print("Name:", validate_stations.name)
    print(f"Crew: {validate_stations.crew_size} People")
    print(f"Power: {validate_stations.power_level}%")
    print(f"Oxygen: {validate_stations.oxygen_level}%")
    print("Data:", validate_stations.last_maintenance)
    if validate_stations.is_operational is True:
        print("Status: Operational")
    else:
        print("Status: Not operational")
    if validate_stations.notes:
        print("Note:", validate_stations.notes)
    print("=" * 30)
    print()

    try:
        _ = SpaceStation(
        station_id="ERR001",
        name="Omega TaeRae SAD",
        crew_size=25,
        power_level=66.5,
        oxygen_level=66.3,
        last_maintenance=datetime.now(),
    )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == '__main__':
    main()