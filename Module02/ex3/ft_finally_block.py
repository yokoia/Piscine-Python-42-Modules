from typing import List


def water_plants(plant_list: List[str]) -> None:
    """Water all plants safely."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception("Error: Cannot water None - invalid plant!")
            else:
                print("Watering", plant)
        print("Watering completed successfully!")
    except Exception as message:
        print(message)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test watering scenarios."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)

    print("\nTesting error watering...")
    plants = ["tomato", None, "carrots"]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
