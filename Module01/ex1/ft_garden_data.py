
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    p1 = Plant("Yucca", 10, 20)
    p2 = Plant("Rose", 20, 40)
    p3 = Plant("Bamboo", 55, 35)
    print("=== Garden Plant Registry ===")
    print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.age} days old")
