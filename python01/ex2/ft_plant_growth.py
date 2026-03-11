class Plant:
	def __init__(self, name: str, age: int, height: int):
		self.name = name
		self.old = age
		self.height = height

	def grow(self):
		self.height += 1
	
	def age(self):
		self.old += 1
	
	def get_info(self):
		print(f"{self.name}: {self.height}cm, {self.old} days old")

def ft_plant_growth():
	day1 = 21
	rose = Plant("rose", 5, 21)
	for day in range(7):
		print(f"=== DAY {day + 1} ===")
		rose.get_info()
		rose.grow()
		rose.age()
	print(f"Growth this week: +{rose.height - day1}cm")

if __name__ == "__main__":
	ft_plant_growth()
	