
class GardenManager:
    total_gardens = 0
    gardens = []

    @staticmethod
    def validate_height(height):
        return height > 0

    class GardenStats:
        @staticmethod
        def count_gardens(gardens):
            return len(gardens)

    @classmethod
    def add_garden(cls, garden):
        cls.gardens.append(garden)
        cls.total_gardens += 1

    @classmethod
    def create_garden_network(cls):
        print("Garden network created")

    @classmethod
    def get_total_gardens(cls):
        return cls.total_gardens


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_plants = 0

    def report(self):
        print("=== Alice's Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if plant.type == "Regular":
                print(f"- {plant.name}: {plant.height}cm")
            elif plant.type == "Flower":
                plant.fp_blooming()
            elif plant.type == "PrizeFlower":
                plant.pf_blooming()

    def add_score(self):
        score = 0
        for plant in self.plants:
            if plant.type == "Flower":
                score = score + 20
            elif plant.type == "Regular":
                score = score + 10
            elif plant.type == "PrizeFlower":
                score = score + 20 + plant.prize
        return score

    def add_plant(self, plant):
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        cm = 0
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")
            cm = cm + 1
        return cm

    def get_plants_info(self, cm):
        count_f = 0
        count_r = 0
        count_pf = 0
        print(f"Plants added: {self.total_plants}, Total growth: "
              f"{cm}cm")
        for plant in self.plants:
            if plant.type == "Regular":
                count_r += 1
            elif plant.type == "Flower":
                count_f += 1
            elif plant.type == "PrizeFlower":
                count_pf += 1
        print(f"Plant types: {count_r} regular, {count_f} flowering, "
              f"{count_pf} prize flowers")


class Plant:
    def __init__(self, name, height, type):
        self.name = name
        self.height = height
        self.type = type

    def grow(self):
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, type, color):
        super().__init__(name, height, type)
        self.color = color

    def fp_blooming(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, type, color):
        super().__init__(name, height, type, color)
        self.prize = 10

    def pf_blooming(self):
        print(f"- {self.name}: {self.height}cm, {self.color} "
              f"flowers (blooming), Prize points: {self.prize}")


def main():
    garden1 = Garden("Alice")
    garden2 = Garden("Bob")
    GardenManager.add_garden(garden1)
    GardenManager.add_garden(garden2)
    plant = [
                Plant("Oak Tree", 100, "Regular"),
                FloweringPlant("Rose", 25, "Flower", "red"),
                PrizeFlower("Sunflower", 50, "PrizeFlower", "yellow")
            ]
    print("=== Garden Management System Demo ===\n")
    for p in plant:
        garden1.add_plant(p)
    print("")
    cm = garden1.grow_all()
    print("")
    garden1.report()
    print("")
    garden1.get_plants_info(cm)
    print("")
    print(f"Height validation test: "
          f"{GardenManager.validate_height(plant[0].height)}")
    print("Garden scores - ", end='')
    for garden in GardenManager.gardens:
        print(f"{garden.owner}: {garden.add_score()}", end='')
        if garden != GardenManager.gardens[-1]:
            print(", ", end='')
    print("")
    print("Total gardens managed: ", end='')
    print(GardenManager.GardenStats.count_gardens(GardenManager.gardens))


if __name__ == "__main__":
    main()
