

def validate_ingredients(ingredients: str) -> str:
    ingrs = ingredients.split()
    valid = ["fire", "water", "earth", "air"]
    for i in ingrs:
        if (i not in valid):
            return (f"{ingredients} - INVALID")
    return (f"{ingredients} - VALID")
