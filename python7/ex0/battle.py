
from ex0.ex0.factories import FlameFactory, AquaFactory


def test_factory(factory):
    print("Testing factory")
    base = factory.create_base()
    evl = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evl.describe())
    print(evl.attack())


def battle(factory1, factory2):
    base = factory1.create_base()
    base1 = factory2.create_base()

    print("Testing battle")
    print(base.describe())
    print(" vs.")
    print(base1.describe())
    print(" fight!")
    print(base.attack())
    print(base1.attack())


if __name__ == '__main__':
    test_factory(FlameFactory())
    print()
    test_factory(AquaFactory())
    print()
    battle(FlameFactory(), AquaFactory())
