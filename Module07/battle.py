
from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:
    print("Testing factory")
    base = factory.create_base()
    envolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(envolved.describe())
    print(envolved.attack())


def battle(factory1, factory2) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())
    print("vs.")
    print(base2.describe())
    print("fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    factory_flame = FlameFactory()
    factory_aqua = AquaFactory()

    test_factory(factory_flame)
    print()
    test_factory(factory_aqua)
    print()
    battle(factory_flame, factory_aqua)
