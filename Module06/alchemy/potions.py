

import alchemy.elements
from alchemy.elements import create_fire


def healing_potion():
    return f"Healing potion brewed with {create_fire()} and \
{alchemy.create_water()}"


def strength_potion():
    return f"Strength potion brewed with {alchemy.elements.create_earth()} \
and {create_fire()}"


def invisibility_potion():
    return f"Invisibility potion brewed with {alchemy.elements.create_air()} \
and {alchemy.create_water()}"


def wisdom_potion():
    return f"Wisdom potion brewed with all elements: {create_fire()} \
{alchemy.create_water()} {alchemy.elements.create_earth()} \
{alchemy.elements.create_air()}"
