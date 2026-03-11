class SecurePlant:
    def __init__(self, name: str):
        self.__name = name
        self.__age = 0
        self.__height = 0
        print(f"Plant created: {self.__name}")

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self):
        return self.__height
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
def ft_garden_security():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(f"Current plant: {plant.get_name()} ({plant.get_height()}cm, {plant.get_age()} days)")

if __name__ == "__main__":
    ft_garden_security()