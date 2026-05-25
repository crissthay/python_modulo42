from .capability import Sproutling, Bloomelle
from .capability import Shiftling, Morphagon
from ex0.ex0.factories import CreatureFactory


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling('Sproutling', 'Grass')

    def create_evolved(self):
        return Bloomelle('Bloomelle', 'Grass/Fairy')


class TransformCreatureFactory(CreatureFactory):

    def create_base(self):
        return Shiftling('Shiftling')

    def create_evolved(self):
        return Morphagon('Morphagon')
