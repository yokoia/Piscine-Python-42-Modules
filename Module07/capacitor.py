
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(healing_factory) -> None:
    print("Testing Creature with healing capability")
    base = healing_factory.create_base()
    evolved = healing_factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(transform_factory) -> None:
    print("Testing Creature with transform capability")
    base = transform_factory.create_base()
    evolved = transform_factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(healing_factory)
    print()
    test_transform(transform_factory)
