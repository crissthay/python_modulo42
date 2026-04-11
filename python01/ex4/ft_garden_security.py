class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0
        else:
            self._height = height

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm")

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days")

    def get_info(self):
        return f"{self.name}: {self._height}cm, {self._age} days old"


def main():
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print("Plant created:", plant.get_info())

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-10)

    print("Current state:", plant.get_info())


if __name__ == "__main__":
    main()
