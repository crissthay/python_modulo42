class Plant:
	def __init__(self, name: str, age: int, height: int):
		self.name = name
		self.age = age
		self.height = height

	def print_data(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
	rose = Plant('Rose', 21, 53)
	sunflower = Plant("Sunflower", 22, 10)
	cactus = Plant("Cactus", 17, 20)

	rose.print_data()
	sunflower.print_data()
	cactus.print_data()

if __name__ == "__main__":
	ft_garden_data()
