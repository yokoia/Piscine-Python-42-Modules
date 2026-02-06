

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", 'w')
        content = ("[ENTRY 001] New quantum algorithm discovered\n" +
                   "[ENTRY 002] Efficiency increased by 347%\n" +
                   "[ENTRY 003] Archived by Data Archivist trainee")
        file.write(content)
        print(content)

    except (FileNotFoundError, PermissionError) as e:
        print("Error:", e)
        file = None

    finally:
        print("\nData inscription complete. Storage unit sealed")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
        if file:
            file.close()
