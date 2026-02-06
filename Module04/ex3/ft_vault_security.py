

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    try:
        with open("classified_data.txt", "r") as file1:
            reading = file1.read()
            print("SECURE EXTRACTION:")
            print(reading)
            print()
    except Exception as message:
        print("Error:", message)
    try:
        with open("security_protocols.txt", 'w') as file2:
            print("SECURE PRESERVATION:")
            data = "[CLASSIFIED] New security protocols archived"
            file2.write(f"\n{data}")
            print(data)
        print("Vault automatically sealed upon completion")
    except Exception as e:
        print("Error:", e)
    finally:
        print("\nAll vault operations completed with maximum security.")
