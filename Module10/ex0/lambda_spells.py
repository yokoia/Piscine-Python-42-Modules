

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)}


def main() -> None:
    print("\nTesting artifact sorter...")

    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'armor'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'focus'}
    ]

    sorting = artifact_sorter(artifacts)
    print(f"{sorting[0]['name']} ({sorting[0]['power']} power)",
          f"comes before {sorting[1]['name']} ({sorting[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transform = spell_transformer(spells)
    print(" ".join(transform))


if __name__ == "__main__":
    main()
