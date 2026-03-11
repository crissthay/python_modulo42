class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.age = age
        self.height = height

class Flower(Plant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade_area} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types():
    print("=== Garden Plant Types ===")
    
    rose = Flower("Rose", 30, 25, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")
    
    oak = Tree("Oak", 1825, 500, 50)
    pine = Tree("Pine", 1460, 400, 40)
    
    tomato = Vegetable("Tomato", 90, 80, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 70, 30, "spring", "vitamin A")
    
    for flower in [rose, tulip]:
        print(f"{flower.name} (Flower): {flower.height}cm, {flower.age} days, {flower.color} color")
        flower.bloom()
    
    for tree in [oak, pine]:
        print(f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, {tree.trunk_diameter}cm diameter")
        tree.produce_shade()
    
    for veg in [tomato, carrot]:
        print(f"{veg.name} (Vegetable): {veg.height}cm, {veg.age} days, {veg.harvest_season} harvest")
        veg.info()


if __name__ == "__main__":
    ft_plant_types()
    