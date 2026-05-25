from ex1.ex1.factorie import HealingCreatureFactory, TransformCreatureFactory


def healing():
    print("Testing Creature with healing capability")
    print(" Base")
    factory = HealingCreatureFactory()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    evl = factory.create_evolved()
    print(evl.describe())
    print(evl.attack())
    print(evl.heal())


def trans():
    print("Testing Creature with transform capability")
    print(" Base")
    factory = TransformCreatureFactory()
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.transformed_attack())
    print(base.revert())

    print(" evolved:")
    evl = factory.create_evolved()
    print(evl.describe())
    print(evl.attack())
    print(evl.transform())
    print(evl.transformed_attack())
    print(evl.revert())


if __name__ == '__main__':
    healing()
    print()
    trans()
