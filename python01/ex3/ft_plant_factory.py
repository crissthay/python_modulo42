class Plant:
	def __init__(self, name: str, age: int, height: int):
		self.name = name
		self.age = age
		self.height = height

def main():
	tipo = [
			Plant("rose", 30, 25),
		 	Plant("Oak", 365, 200),
			Plant("Cactus", 90, 5),
			Plant("Sunflower", 45, 80),
			Plant("Fern", 120, 15)
			]
	print("=== Plant Factory Output ===")
	for plant in tipo:
		print(f"created: {plant.name} ({plant.height}cm, {plant.age} days)")

main()