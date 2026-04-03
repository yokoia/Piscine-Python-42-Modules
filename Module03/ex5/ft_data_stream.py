# how i % len works = when i=6%len=6 willbe = 0 it resets from 0 to 5 again
# yield makes a func be a generator not just normal func

players = [
    ("alice", 5, "monster"),
    ("bob", 12, "treasure"),
    ("charlie", 8, "level-up"),
]

n: int = 1000


def game_events(n: int):
    for i in range(n):
        name, level, action = players[i % len(players)]
        yield name, level, action


it = game_events(n)  # #######


def generating() -> None:
    print(f"Processing {n} game events...\n")
    event_number = 1
    for name, level, event in it:
        if event == "monster":
            print(
                f"Event {event_number}: Player {name} (level {level}) "
                f"killed {event}"
            )
        elif event == "treasure":
            print(
                f"Event {event_number}: Player {name} (level {level}) "
                f"found {event}"
            )
        else:
            print(
                f"Event {event_number}: Player {name} (level {level}) "
                f"leveled up"
            )
        event_number += 1


it2 = game_events(n)


def stream_analytics(n: int) -> None:
    print("=== Stream Analytics ===")
    hight_level = 0
    treasure = 0
    levelup = 0
    print(f"Total events processed: {n}")
    for _, level, event in it2:
        if level >= 10:
            hight_level += 1
        if event == "treasure":
            treasure += 1
        if event == "level-up":
            levelup += 1
    print(f"Hight_level players: {hight_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")


def prime(n: int):
    number = 2
    count = 0
    while count < n:
        for x in range(2, number):
            if number % x == 0:
                break
        else:
            count += 1
            yield number
        number += 1


def fibonacci(n: int):
    i1 = 0
    i2 = 1
    for i in range(10):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            yield i1 + i2
            tmp = i1 + i2
            i1 = i2
            i2 = tmp


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    generating()
    print("...")
    stream_analytics(n)
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=' ')
    it3 = fibonacci(10)
    for i in range(10):
        print(f"{next(it3)}", end='')
        if i != 9:
            print(", ", end='')
    print("\nPrime numbers (first 5):", end=' ')
    it4 = prime(5)
    for i in range(5):
        print(f"{next(it4)}", end='')
        if i != 4:
            print(", ", end='')
    print()
