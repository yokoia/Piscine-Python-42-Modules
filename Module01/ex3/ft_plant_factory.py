
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


plants_data = [
    ("Yucca", 10, 20),
    ("Rose", 20, 40),
    ("Bamboo", 55, 35),
    ("Sunflower", 80, 45),
    ("cactus", 15, 120)
]
plants = [None, None, None, None, None]
count = 0

if __name__ == "__main__":
    for i in range(5):
        plants[i] = Plant(*plants_data[i])
        count = count + 1

    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created:", end=' ')
        print(f"{plant.name} ({plant.height}cm, {plant.age} days)")
    print("\nTotal plants created:", count)
