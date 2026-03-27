
from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.validation_a_h(attack, health)

    def validation_a_h(self, a, h) -> None:
        if not isinstance(a, int) or a <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(h, int) or h <= 0:
            raise ValueError("health must be a positive integer")
        self.attack = a
        self.health = h

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "attack": self.attack,
                "health": self.health
                }

    def play(self, game_state: dict) -> dict:
        if (not self.is_playable(game_state["mana_left"])):
            return ({
                "card_played": None,
                "mana_used": 0,
                "effect": None
            })
        self.attack_target(game_state["target"])
        return ({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        })

    def attack_target(self, target) -> dict:
        # damage dealt: the amount of damage i caused to the enemy
        try:
            if (self.health <= 0 or target.health <= 0):
                return {
                    "attacker": self.name,
                    "target": target.name,
                    "damage_dealt": 0,
                    "combat_resolved": False
                }
        except KeyError:
            return {"target": "Not a valid target"}
        if target.health < self.attack:
            actual_damage = target.health  # store the real damage
            target.health = 0
            return {
                    "attacker": self.name,
                    "target": target.name,
                    "damage_dealt": actual_damage,
                    "combat_resolved": True
                }
        else:
            target.health = target.health - self.attack
            return {
                        "attacker": self.name,
                        "target": target.name,
                        "damage_dealt": self.attack,
                        "combat_resolved": True
                    }

