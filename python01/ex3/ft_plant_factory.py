class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.days_old = age
        self.height = height

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.days_old} days)"


def main():
    plants = [
        Plant("Rose", 30, 25),
        Plant("Oak", 365, 200),
        Plant("Cactus", 90, 5),
        Plant("Sunflower", 45, 80),
        Plant("Fern", 120, 15)
    ]

    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created:", plant.get_info())


if __name__ == "__main__":
    main()
