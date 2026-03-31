
from ex0.Card import Card, CardType
from ex0.CreatureCard import CreatureCard
from typing import Dict, List
from enum import Enum


class EffectType(Enum):
    DAMAGE = "Deal 3 damage to target"
    HEAL = "Heal 3 health"
    BUFF = "Apply buff to the ally creature"
    DEBUFF = "Apply debuff to enemy creature"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: EffectType) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = CardType.SPELL.value

    def play(self, game_state: dict) -> Dict:
        out = {
            "card_played": None,
            "mana_used": 0,
            "effect": None
        }
        if (not self.is_playable(game_state["mana_left"])):
            return (out)
        game_state['mana_left'] = game_state['mana_left'] - self.cost
        self.resolve_effect(game_state["targets"])
        return ({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type.value
        })

    def resolve_effect(self, targets: List[CreatureCard]) -> Dict:
        try:
            if (self.effect_type == EffectType.DAMAGE):
                for t in targets:
                    t.health -= 3
                return ({"effect": self.effect_type.value})
            elif (self.effect_type == EffectType.HEAL):
                for t in targets:
                    t.health += 3
                return ({"effect": self.effect_type.value})
            elif (self.effect_type == EffectType.BUFF):
                for t in targets:
                    t.attack += 3
                return ({"effect": self.effect_type.value})
            elif (self.effect_type == EffectType.DEBUFF):
                for t in targets:
                    t.attack -= 3
                return ({"effect": self.effect_type.value})
        except Exception as e:
            print("Error in resolve_effect:", e)
            return ({"effect": None})
        return ({"effect": None})
