class Plant:
    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant._Stats()

    def grow(self):
        self._height += 8
        self._stats.grow_calls += 1

    def age_up(self):
        self._age += 1
        self._stats.age_calls += 1

    def show(self):
        print(
            f"{self.name}: {self._height}cm, "
            f"{self._age} days old"
        )
        self._stats.show_calls += 1

    def display_stats(self):
        self._stats.display()

    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(
                f"{self.name} is blooming "
                f"beautifully!"
            )
        else:
            print(
                f"{self.name} has not "
                f"bloomed yet"
            )


class Tree(Plant):
    def __init__(self, name, height, age,
                 trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade "
            f"of {self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )
        self._shade_calls += 1

    def display_stats(self):
        super().display_stats()
        print(f"{self._shade_calls} shade")

    def show(self):
        super().show()
        print(
            f"Trunk diameter: "
            f"{self.trunk_diameter}cm"
        )


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def show_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old ===")
    print(
        "Is 30 days more than a year? ->",
        Plant.is_older_than_year(30)
    )
    print(
        "Is 400 days more than a year? ->",
        Plant.is_older_than_year(400)
    )

    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_statistics(rose)

    print("=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)

    print("=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    sunflower.show()
    show_statistics(sunflower)

    print("=== Anonymous ===")
    unknown = Plant.anonymous()
    unknown.show()
    show_statistics(unknown)


if __name__ == "__main__":
    main()
