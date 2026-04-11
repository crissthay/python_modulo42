class PlantError(Exception):
    def __init__(self, message="Caught PlantError"):
        Exception.__init__(self, message)


def water_plant(plant_name: str):
    try:
        if plant_name != plant_name.capitalize():
            raise PlantError(f"Invalid plant name to water: {plant_name}")

        print(f"Watering {plant_name}: [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        raise
    finally:
        pass


def test_watering_system():
    print("=== Garden Watering System ===\n")

    try:
        print("Testing valid plants...")
        print("Opening watering system")

        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")

    except PlantError:
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        water_plant("tomato")
        water_plant("lettuce")

    except PlantError:
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


def main():
    test_watering_system()


if __name__ == "__main__":
    main()
