

def check_temperature(temp_str: str) -> None:
    """Validate and check plant-safe temperature."""
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    return None


def test_temperature_input() -> None:
    """Run sample temperature tests."""
    print("=== Garden Temperature Checker ===\n")
    test_values = ["25", "abc", "100", "-50"]
    for temp in test_values:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print("")
    print("All tests completed - program didn't crash!")


test_temperature_input()
