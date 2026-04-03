

class GardenError(Exception):
    """Base garden error."""
    pass


class PlantError(GardenError):
    """Plant-related error."""
    pass


class WaterError(GardenError):
    """Water-related error."""
    pass


class GardenManager:
    """Manage garden operations."""

    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        """Add a plant to the garden."""
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print("Error adding plant:", e)

    def water_plants(self, water: int) -> None:
        """Water all plants."""
        print("Opening watering system")
        try:
            if water < 50:
                raise WaterError("Not enough water in tank")
            for plant in self.plants:
                print("Watering", plant, "- success")
        except WaterError as e:
            print("Water error:", e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int,
        sun: int
    ) -> None:
        """Check plant health."""
        try:
            if plant_name not in self.plants:
                raise PlantError("Plant not found")
            if water_level < 1 or water_level > 10:
                raise PlantError(
                    f"Water level {water_level} is too low/high "
                    "(min 1, max 10)"
                )
            if sun < 2 or sun > 12:
                raise PlantError(
                    f"Sun {sun} is too high/low (min 2, max 12)"
                )
            print(f"{plant_name}: healthy (water: {water_level}, sun: {sun})")
        except PlantError as e:
            print(f"Error checking {plant_name}:", e)


def test_garden_management() -> None:
    """Test garden manager."""
    print("=== Garden Management Test ===\n")

    manager: GardenManager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("Tomato")
    manager.add_plant("")
    manager.add_plant("Lettuce")

    print("\nWatering plants...")
    manager.water_plants(100)
    manager.water_plants(60)

    print("\nChecking plant health...")
    manager.check_plant_health("Tomato", 5, 8)
    manager.check_plant_health("Tomato", 15, 8)
    manager.check_plant_health("Potato", 15, 8)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in the tank")
    except GardenError as message:
        print("Caught GardenError:", message)
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


test_garden_management()
