
from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name) -> None:
        Card.__init__(self, name, 6, "Epic")
        Combatable.__init__(self, 5)
        self.mana = 8
        self.health = 10

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health = self.health - incoming_damage
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": max(0, self.damage - incoming_damage),
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.damage,
            "health": self.health,
            "defense_block": 3,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        if self.mana < mana_used:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": 0
            }
        self.mana -= mana_used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_left": self.mana,
            "spell_name": "Fireball"
        }

    def play(self, game_state: dict) -> dict:
        if game_state.get("phase") == "combat":
            return self.attack("Enemy")
        if game_state.get("phase") == "magic":
            return self.cast_spell("Fireball", ['Enemy1', 'Enemy2'])
        return {
            "card_played": self.name,
            "effect": "No phase action",
        }
