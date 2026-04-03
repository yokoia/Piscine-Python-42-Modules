
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(self, height)
        self.set_age(self, age)
        print(f"Plant Created: {self.name}")

    def set_height(self, height):
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print("Invalid operation attempted:", end=' ')
            print(f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print("Invalid operation attempted:", end=' ')
            print(f"age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Yucca", 10, 50)
    height = plant.set_height(25)
    age = plant.set_age(30)
    print("")
    plant.set_height(-5)
    print("")
    print(f"Current plant: {plant.name}", end=' ')
    print(f"({plant.get_height()}cm, {plant.get_age()} days)")
