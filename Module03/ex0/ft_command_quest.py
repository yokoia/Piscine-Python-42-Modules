

import sys

if __name__ == "__main__":
    argc: int = len(sys.argv)
    print("=== Command Quest ===")
    if argc == 1:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
        print("Total arguments:", argc)
    else:
        print("Program name:", sys.argv[0])
        print("Arguments received:", argc - 1)
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {argc}")
