
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

    def play(self, game_state: dict) -> dict:
        out = {
            "card_played": None,
            "mana_used": 0,
            "effect": None
        }
        if (not self.is_playable(game_state["mana_left"])):
            return (out)
        self.activate_ability()
        game_state['mana_left'] = game_state['mana_left'] - self.cost
        return ({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        })

    def activate_ability(self) -> dict:
        return ({"effect": self.effect})
