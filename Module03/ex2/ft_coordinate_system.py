
import sys
import math


def main() -> None:
    ac: int = len(sys.argv)
    print("=== Game Coordinate System ===\n")
    print("Example:")
    a1, b1, c1 = origin = (0, 0, 0)
    a2, b2, c2 = position = (10, 20, 5)
    d: float = math.sqrt((a2-a1)**2 + (b2-b1)**2 + (c2-c1)**2)
    print("Position created:", position)
    print(f"Distance between {origin} and {position}: {d:.2f}\n")

    if ac == 2:
        try:
            argv: list[str] = sys.argv[1].split(',')
            listt: list[int] = []
            for list_item in argv:
                number: int = int(list_item)
                listt.append(number)
            x1, y1, z1 = tupple1 = (0, 0, 0)

            print(f"Parsing coordinates: \"{sys.argv[1]}\"")
            x2, y2, z2 = tupple2 = tuple(listt)
            print("Position created:", tupple2)
            distance: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(f"Distance between {tupple1} and {tupple2}: "
                  f"{distance:.2f}\n")
        except ValueError as message:
            print("The argument must be like: <4,5,-18>")
            print(f"\nParsing invalid coordinates: {sys.argv[1]}")
            print("Error parsing coordinates:", message)
            print(f"Error details - Type: {type(message).__name__}, Args: "
                  f"(\"{message}\")")
            return
    else:
        print("you must to pass coordinates in one argument only")
        return

    print("\nUnpacking demonstration:")
    print(f"Player: x = {x2}, y= {y2}, z = {z2}")
    print(f"Player: X = {x2}, Y= {y2}, Z = {z2}")


if (__name__ == "__main__"):
    main()
