
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade:.0f} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def vitamin(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


if __name__ == "__main__":
    flower = [Flower("Rose", 25, 30, "red"), Flower("Iris", 23, 51, "purple")]
    tree = [Tree("Oak", 500, 1825, 50), Tree("Maple", 55, 114, 10)]
    vegetable = [Vegetable("Tomato", 80, 90, "summer harvest", "C"),
                 Vegetable("Spinach", 27, 30, "spring", "C")]
    print("=== Garden Plant Types ===\n")
    print(
        f"{flower[0].name} (Flower): {flower[0].height}cm, "
        f"{flower[0].age} days, {flower[0].color} color"
        )
    flower[0].bloom()
    print("")
    print(
        f"{tree[0].name} (Tree): {tree[0].height}cm, "
        f"{tree[0].age} days, {tree[0].trunk_diameter} diameter"
        )
    tree[0].produce_shade()
    print("")
    print(
        f"{vegetable[0].name} (Vegetable): {vegetable[0].height}cm, "
        f"{vegetable[0].age} days, {vegetable[0].harvest_season}"
        )
    vegetable[0].vitamin()
