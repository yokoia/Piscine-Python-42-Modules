
# set(a): puts them without duplicate
# a.union(b): join sets a and b in a 1 set without duplicate
# a.intersection(b): set nums in a that appears in b
# a.difference(b): set nums in set1 that are not in set2

alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
           'perfectionist'}


def achievement_tracker() -> None:
    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)


def achievement_analytics() -> None:
    print("\n=== Achievement Analytics ===")
    total = alice.union(bob, charlie)
    print("All unique achievements:", total)
    print("Total unique achievements:", len(total))


def commom_rare() -> None:
    diff1 = alice.difference(bob, charlie)
    diff2 = bob.difference(alice, charlie)
    diff3 = charlie.difference(alice, bob)
    join = diff1.union(diff2, diff3)
    print("\nCommon to all players:", alice.intersection(bob, charlie))
    print("Rare achievements (1 player):", join)


def alice_bob() -> None:
    print("\nAlice vs Bob common:", alice.intersection(bob))
    print("Alice unique:", alice.difference(bob))
    print("Bob unique:", bob.difference(alice))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievement_tracker()
    achievement_analytics()
    commom_rare()
    alice_bob()
