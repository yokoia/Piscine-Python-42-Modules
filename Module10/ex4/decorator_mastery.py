
from functools import wraps
from typing import Callable
import time
# staticmethod for func that doesnt use self but still inside a class
# wrap: “copy metadata from func into wrapper”, returns a helper that modifies

#1- power_validator(10)
#2 - decorator(cast_spell) automatic part
def spell_timer(func: Callable) -> Callable:
    @wraps(func)  # makes the wrapper function look like the original function
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:  # we pass the func first
        @wraps(func)
        def wrapper(*args, **kwargs):  # then we make a wrapperr
            power = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}"
                              f"/{max_attempts})")
                    else:
                        print("Spell casting failed after "
                              f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name))

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


############# functions for test ##############

@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def spell(x: int) -> str:
    if x < 0:
        raise Exception("ERROR")
    return "Waaaaaaagh spelled !"


################################################
def main() -> None:
    print("Testing spell timer...")
    func = fireball()
    print("Result:", func)

    print("\nTesting retrying spell...")
    spell(-1)
    success= spell(2)
    print(success)

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Youssra Koia"))
    print(MageGuild.validate_mage_name("Youssra 1337"))
    instance = MageGuild()
    msg = instance.cast_spell("Lightning", 15)
    invalid_msg = instance.cast_spell("Lightning", 9)
    print(f"{msg}\n{invalid_msg}")


main()
