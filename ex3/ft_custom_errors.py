class GardenError(Exception):
    def __init__(self, message = "Unknown Garden Error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message = "Plant Error") :
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message = "Water Error"):
        super().__init__(message)

def ErrorTester() -> None:
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}", end="\n\n")
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}", end="\n\n")
    try:
        print("Testing catching all garden errors...")
        raise GardenError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}", end="\n\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===", end="\n\n")
    ErrorTester()
    print("All custom error types work correctly!")
