
# dict(): makes a dictionary
# keys(): returns a list of names in dict
# values(): returns a list of only values in dic
# items(): returns a list of tupples (names, values)
# get("name"): gets the value of a name
# update({"b": 2, "a": 10}): updates values

import sys

try:
    inventory: dict = dict()
    for av in sys.argv[1:]:
        name, qty = av.split(':')
        if int(qty) < 0:
            raise ValueError("Quantity can not be negative!")
        inventory[name] = int(qty)

    total: int = 0
    for val in inventory.values():
        total += val
    quantity: int = len(inventory)
    items: list = inventory.items()
    values: list = inventory.values()

except Exception as message:
    print("Error:", message)


def system_analysis() -> None:
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {quantity}")


def current() -> None:
    print("\n=== Current Inventory ===")
    for key, v in items:
        print(f"{key}: {v} units ({((v / total) * 100):.1f}%)")


def statistics() -> None:
    print("\n=== Inventory Statistics ===")
    maxx = max(values)
    minn = min(values)
    for key, v in items:
        if maxx == v:
            print("Most abundant:", end=' ')
            print(f"{key} ({v} units)")
        if minn == v:
            print("Least abundant:", end=' ')
            if minn > 1:
                print(f"{key} ({v} units)")
            else:
                print(f"{key} ({v} unit)")


def categories() -> None:
    print("\n=== Item Categories ===")
    new: dict = {
        "Moderate": {},
        "Scarce": {}
    }
    for key, v in items:
        if v < 5:
            new["Scarce"][key] = v
        else:
            new["Moderate"][key] = v
    print(f"Moderate: {new['Moderate']}")
    print(f"Scarce: {new['Scarce']}")


def management() -> None:
    print("\n=== Management Suggestions ===")
    new = []
    for key, v in items:
        if v <= 1:
            new.append(key)
    print(f"Restock needed: {new}")


def dic_properties() -> None:
    print("\n=== Dictionary Properties Demo ===")
    new_dic = []
    new_val = []
    for name, _ in inventory.items():
        new_dic.append(name)
    for _, v in inventory.items():
        new_val.append(v)
    print("Dictionary keys:", new_dic)
    print("Dictionary values:", new_val)
    print("Sample lookup - 'sword' in inventory:", end=' ')
    print(inventory.get("sword") is not None)


def main():
    argc = len(sys.argv)
    if argc <= 1:
        print("Error: You need at least one argument!")
        print("Arguments must be passed only like: <item:quantity>")
        return
    try:
        system_analysis()
        current()
        statistics()
        categories()
        management()
        dic_properties()
    except Exception as message:
        print("error", message)
        return


if __name__ == "__main__":
    main()
