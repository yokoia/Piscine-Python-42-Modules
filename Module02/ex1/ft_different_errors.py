
def garden_operations() -> None:
    """Demonstrate common Python errors."""
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        missing = {"tree": 5}
        missing["tre"]
    except KeyError:
        print("Caught KeyError: 'missing/_tre'\n")


def test_error_types() -> None:
    """Run error handling tests."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    finally:
        print("All error types tested successfully!")


test_error_types()
