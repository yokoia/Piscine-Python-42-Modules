
import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    input1 = input("Input Stream active. Enter archivist ID: ")
    input2 = input("Input Stream active. Enter status report: ")
    sys.stdout.write("\n")
    sys.stdout.write(f"[STANDARD] Archive status from "
                     f"{input1.strip()}: {input2.strip()}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                     "verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")
