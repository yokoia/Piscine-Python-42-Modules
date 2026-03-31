from ex1.Deck import Deck
from ex0.Card import Rarity
from .SpellCard import SpellCard, EffectType
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


if (__name__ == "__main__"):
    print("=== DataDeck Deck Builder ===\n")

    creature = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
    spell = SpellCard("Lightning Bolt", 3,
                      Rarity.RARE, EffectType.DAMAGE)
    artifact = ArtifactCard("Mana Crystal", 4,
                            Rarity.COMMON, 4, "Permanent: +1 mana per turn")

    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)
    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")
    deck.shuffle()
    gob = CreatureCard("Gobelin Warrior", 1, Rarity.COMMON, 2, 3)
    game = {
        "target": gob,
        "targets": [gob],
        "mana_left": 100
    }
    while deck.cards:
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type})")
        print(f"Play result: {card.play(game)}")
        print()

    print("\nPolymorphism in action: Same interface,"
          "different card behaviors!")
