# nonlocal lets u modify outer variables not just read them
# nonlocal also remember the variable last value
# nonlocal is ONLY used inside the inner (nested) function
# closures is the way nested funcs remember their variables

from typing import Callable


def mage_counter() -> Callable:
    count = 0  # executed only once when u call func = mage_counter()
    # not when u call func()
    def count_calls() -> int:
        nonlocal count
        count += 1
        return count
    return count_calls
    

def spell_accumulator(initial_power: int) -> Callable:
    result = initial_power
    def add_power(value: int) -> int:
        nonlocal result
        result += value
        return result
    return  add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    ench = enchantment_type
    def add_ench(item_name: str) -> str:
        nonlocal ench
        ench = ench + item_name
        return ench
    return add_ench


def memory_vault() -> dict[str, Callable]:
    shared_memory = {}  # Mutable objects

    def store(key: str, value: int) -> None:
        shared_memory[key] = value

    def recall(key: str) -> str | int:
        if key in shared_memory:
            return shared_memory[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_a call 1:", counter_b())

    print("\nTesting spell accumulator...")
    base = spell_accumulator(100)
    print("Base 100, add 20:", base(20))
    print("Base 100, add 30:", base(30))

    print("\nTesting enchantment factory...")
    ench1 = enchantment_factory("Flaming")
    ench2 = enchantment_factory("Frozen")
    print(ench1("Sword"))
    print(ench1("Shield"))

    print("\nTesting memory vault...")
    memory: Callable = memory_vault()
    memory['store']("secret", 42)
    print("Store 'secret' = 42")
    recall: str | int = memory['recall']("secret")
    print(f"Recall: 'secret': {recall}")
    recall: str | int = memory['recall']("invalid")
    print(f"Recall: 'secret': {recall}")


main()