

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any

# reduce: work with iterators join first with scnd...
# partial: returns a func like object with fixed args and u can add args later
# lru_cache: It stores the return of a func, so when u call it again with same input
#     it return the result faster than recomputing it again
# singledispatch: chooses funcs according to the parameter type hint


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)

    elif operation == "max":
        return reduce(max, spells)

    elif operation == "min":
        return reduce(min, spells)
    elif not operation:
        return 0
    else:
        raise ValueError("Unknown operation!")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    # partial takes a func, fixed args 50 + fire.. and the target is open
    # when u call fire(u give target here)
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "water": partial(base_enchantment, 50, "water"),
        "earth": partial(base_enchantment, 50, "earth"),
    }


@lru_cache(maxsize=None)  # None: store all results no limit
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell):
        return "Unknown spell type"

    @cast.register(int)  # register is a feature in single...
    def _(spell):
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell):
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells"
    return cast


def main() -> None:
    try:
        print("\nTesting spell reducer...")
        spells = [40, 10, 30, 20]
        print(f"Sum: {spell_reducer(spells, "add")}")
        print("Product: 240000")
        print(f"Max: {spell_reducer(spells, "max")}")

        print("\nTesting memoized fibonacci...")
        print(f"Fib(0):", memoized_fibonacci(0))
        print(f"Fib(1):", memoized_fibonacci(1))
        print(f"Fib(10):", memoized_fibonacci(10))
        print(f"Fib(15):", memoized_fibonacci(15))

        print("\nTesting spell dispatcher...")
        cast = spell_dispatcher()
        print(cast(42))
        print(cast("fireball"))
        print(cast([1, 2, 6]))
        print(cast({"invalid": 10}))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()