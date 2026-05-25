from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def attack(self):
        return f"{self.name} uses Ember!"

    def describe(self):
        return super().describe()


class Pyrodon(Creature):
    def attack(self):
        return f"{self.name} uses Flamethrower!"

    def describe(self):
        return super().describe()


class Aquabub(Creature):
    def attack(self):
        return f"{self.name} uses Water Gun!"

    def describe(self):
        return super().describe()


class Torragon(Creature):
    def attack(self):
        return f"{self.name} uses Hydro Pump!!"

    def describe(self):
        return super().describe()
