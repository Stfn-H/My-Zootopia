import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as file:
    return json.load(file)


def print_animal_data(animal):
    """Print relevant information about a single animal."""
    # Name (top-level)
    if "name" in animal:
        print(f"Name: {animal['name']}")

    # Diet (nested)
    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        print(f"Diet: {characteristics['diet']}")

    # First location (list)
    locations = animal.get("locations", [])
    if locations:
        print(f"Location: {locations[0]}")

    # Type (nested)
    if "type" in characteristics:
        print(f"Type: {characteristics['type']}")

    print()


def main():
    animals = load_data("data/animals_data.json")

    for animal in animals:
        print_animal_data(animal)


if __name__ == "__main__":
    main()
