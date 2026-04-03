

if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print("Accessing Storage Vault: ancient_fragment.txt "
              "Connection established...\n")
        file = open("ancient_fragment.txt", 'r')
        reading = file.read()
        print(reading)
        print("\nData recovery complete. Storage unit disconnected.")
    except Exception as e:
        print("Error:", e)
        file = None
    finally:
        if file:
            file.close()
