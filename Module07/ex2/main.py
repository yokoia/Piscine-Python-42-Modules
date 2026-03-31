
from .EliteCard import EliteCard


if (__name__ == "__main__"):
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    elite = EliteCard("Arcane Warrior")
    print("Playing Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    print("Attack result:", elite.play({"phase": "combat"}))
    print("Defense result:", elite.defend(2))

    print("\nMagic phase:")
    print("Spell cast:", elite.play({"phase": "magic"}))
    print("Mana channel:", elite.channel_mana(3))
    print("\nMultiple interface implementation successful!")
