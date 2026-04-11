class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.days_old = age
        self.height = height

    def grow(self):
        self.height += 1

    def grow_older(self):
        self.days_old += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.days_old} days old"


def ft_plant_growth():
    rose = Plant("Rose", 21, 25)

    initial_height = rose.height

    print("=== Garden Plant Growth ===")

    for day in range(7):
        rose.grow()
        rose.grow_older()

        print(f"=== Day {day + 1} ===")
        print(rose.get_info())

    print(f"Growth this week: {rose.height - initial_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
