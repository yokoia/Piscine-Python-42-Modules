
class GardenError(Exception):
    """Base garden exception."""
    pass


class PlantError(GardenError):
    """Plant-related error."""
    pass


class WaterError(GardenError):
    """Water-related error."""
    pass


def ft_check_plants(days: int, pname: str) -> None:
    """Check plant health."""
    if days > 2:
        raise PlantError(f"The {pname} plant is wilting!")


def ft_check_water(water: int) -> None:
    """Check water level."""
    if water < 50:
        raise WaterError("Not enough water in the tank!")


def main(days: int, water: int, pname: str) -> None:
    """Run garden error tests."""
    print("Testing PlantError...")
    try:
        ft_check_plants(days, pname)
    except PlantError as message:
        print("Caught PlantError:", message)
    print()

    print("Testing WaterError...")
    try:
        ft_check_water(water)
    except WaterError as message:
        print("Caught WaterError:", message)
    print()

    print("Testing catching all garden errors...")
    try:
        ft_check_plants(days, pname)
    except GardenError as message:
        print("Caught a garden error:", message)

    try:
        ft_check_water(water)
    except GardenError as message:
        print("Caught a garden error:", message)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    main(3, 23, "tomato")
