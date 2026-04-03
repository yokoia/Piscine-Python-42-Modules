
from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability, TransformCapability
from ex0.creature import Creature

# healing after the attack
# transform then attack then revert


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}'"
                            "for this aggressive strategy")

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(f"Invalid Creature '{creature.name}'"
                            "for this defensive strategy")

        print(creature.attack())
        print(creature.heal())
