from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature):
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self):
        super().__init__("Normal")

    def is_valid(self, creature) -> bool:
        return creature is not None

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature "
                f"'{creature.name}' for this strategy"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def __init__(self):
        super().__init__("Agressive")

    def is_valid(self, creature) -> bool:
        from ex1.ex1.capability import TransformCapability
        return isinstance('creature', TransformCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature "
                f"'{creature.name}' for this agressive strategy"
            )
        return (
            f"{creature.transform()}, {creature.attack()}, "
            f"{creature.revert()}"
        )


class DefensiveStrategy(BattleStrategy):
    def __init__(self):
        super().__init__("Defensive")

    def is_valid(self, creature) -> bool:
        from ex1.ex1.capability import HealCapability
        return isinstance('creature', HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature "
                f"'{creature.name}' for this defensive strategy"
            )
        return f"{creature.attack()}, {creature.heal()}"
