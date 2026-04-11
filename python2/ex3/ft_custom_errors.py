class GardenError(Exception):
    def __init__(self, message="error"):
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message="Caught PlantError"):
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message="Caught WaterError"):
        GardenError.__init__(self, message)


def test_errors():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!\n")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


def main():
    test_errors()


if __name__ == "__main__":
    main()
