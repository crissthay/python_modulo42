from abc import ABC, abstractmethod
from ex0.ex0.creature import Creature


class HealCapability(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.transformed = False

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self):
        return f"{self.name} uses Vine Whip!"

    def heal(self):
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def __init__(self, name, type):
        super().__init__(name, type)

    def attack(self):
        return f"{self.name} Petal Dance!"

    def heal(self):
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self, name):
        Creature.__init__(self, name, "Normal")
        TransformCapability.__init__(self)

    def transform(self):
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} returns to normal."

    def transformed_attack(self):
        return f"{self.name} performs a boosted strike!"

    def attack(self):
        if self.transformed:
            return self.transformed_attack()
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name):
        Creature.__init__(self, name, "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self):
        self.transformed = True
        return f"{self.name} into a dragonic battle form!"

    def revert(self):
        self.transformed = False
        return f"{self.name} stabilizes its form."

    def transformed_attack(self):
        return f"{self.name} unleashes a devastating morph strike!"

    def attack(self):
        if self.transformed:
            return self.transformed_attack()
        return f"{self.name} attacks normally."
