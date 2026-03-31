
from abc import ABC, abstractmethod


class CardFactory(ABC):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:

    def create_spell(self, name_or_power: str | int | None = None) -> Card:

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

    def create_themed_deck(self, size: int) -> dict:

    def get_supported_types(self) -> dict:

