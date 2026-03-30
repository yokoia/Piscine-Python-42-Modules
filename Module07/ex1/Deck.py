from random import shuffle
from ex0.Card import Card
from typing import Dict, List
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        x = 0
        for card in self.cards[:]:
            if card.name == card_name:
                self.cards.remove(card)
                x = 1
        return x == 1

    def shuffle(self) -> None:

    def draw_card(self) -> Card:

    def get_deck_stats(self) -> dict:
