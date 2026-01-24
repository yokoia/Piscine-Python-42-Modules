
class Plant:
    day = 7

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.old = age

    def grow(self):
        self.height = self.height + 1

    def age(self):
        self.old = self.old + 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.old} days old")


if __name__ == "__main__":
    print("=== Day 1 ===")
    p1 = Plant("Yucca", 10, 20)
    print(f"{p1.name}: {p1.height}cm, {p1.old} days old")
    print(f"=== Day {p1.day} ===")
    old_height = p1.height

    for _ in range(1, p1.day):
        p1.grow()
        p1.age()

    p1.get_info()
    growth = p1.height - old_height
    print(f"Growth this week: +{growth}cm")
