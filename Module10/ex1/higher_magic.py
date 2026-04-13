
from typing import Callable

# first class citizen: funcs can be passed as args and get returned
# callable: type hint: this variable must be a func or behave like it
# callable[int(arg), int(return value)]


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> Callable:
        return spell1(*args, **kwargs), spell2(*args, **kwargs)
    return combined


def power_amplifier(base_spell, multiplier) -> Callable:
    def new_spell(*args, **kwargs) -> Callable:
        new_args = []
        for arg in args:
            new_args.append(arg * multiplier)
        return base_spell(*new_args, **kwargs)
        # *new_args to pass list as tuple args not list
    return new_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_spells(*args, **kwargs) -> list:
        result_spells = []
        for spell in spells:
            result_spells.append(spell(*args, **kwargs))
        return result_spells

    return cast_spells


# ############## fucntions for testing ######################
def fireball(name: str) -> str:
    return f"Fireball hits {name}"


def heal(name: str) -> str:
    return f"Heals {name}"


def base_spell(original) -> int:
    return original


# ########################
def main() -> None:
    print("\nTesting spell combiner...")
    combiner = spell_combiner(fireball, heal)
    r1, r2 = combiner("Dragon")
    print(f"Combined spell result: {r1}, {r2}")

    print("\nTesting power amplifier...")
    amplifier = power_amplifier(base_spell, 3)
    print(f"Original: {base_spell(10)}, Amplified: {amplifier(10)}")


if __name__ == "__main__":
    main()