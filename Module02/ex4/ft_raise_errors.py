

def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    """Check plant health values."""
    try:
        if plant_name is None or plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
        else:
            print("Plant 'tomato' is healthy!")

        if water_level < 1 or water_level > 10:
            raise ValueError(
                f"Error: Water level {water_level} is too "
                "low/high (min 1, max 10)"
            )
        else:
            print("water level is healthy!")

        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too "
                f"low/high (min 2, max 12)"
            )
        else:
            print("sunlight hours is healthy!")
    except ValueError as message:
        print(message)


def test_plant_checks() -> None:
    """Run plant health tests."""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("Bamboo", 5, 8)
    print("\nTesting empty plant name...")
    check_plant_health("", 5, 8)
    print("\nTesting bad water level...")
    check_plant_health("Bamboo", 11, 8)
    print("\nTesting bad sunlight hours...")
    check_plant_health("Bamboo", 5, 1)
    print("\nAll error raising tests completed!")


test_plant_checks()
