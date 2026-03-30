
from .CreatureCard import CreatureCard
from .Card import Rarity


if (__name__ == "__main__"):
    print("=== DataDeck Card Foundation ===\n")

    try:
        dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
        print("Testing Abstract Base Class Design:\n")
        print("CreatureCard Info:")
        print(dragon.get_card_info())
        print("\nPlaying Fire Dragon with 6 mana available:")
        print("Playable:", dragon.is_playable(6))
        goblin = CreatureCard("Goblin Warrior", 2, Rarity.COMMON.value,
                              2, 3)
        print("Play result:", dragon.play({
            "target": goblin,
            "mana_left": 10
            }))

        print("\nFire Dragon attacks Goblin Warrior:")
        print("Attack result:", dragon.attack_target(goblin))
        print("\nTesting insufficient mana (3 available):")
        print("Playable:", dragon.is_playable(3))
        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print("Error", e)
