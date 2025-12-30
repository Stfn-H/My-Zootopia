import json


def load_data(file_path):
  """Loads a JSON file"""
  with open(file_path, "r", encoding="utf-8") as file:
    return json.load(file)


def load_template(file_path):
    """Read and return the HTML template as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal):
    """Serialize a single animal dictionary into an HTML list item."""
    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    locations = animal.get("locations", [])
    if locations:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'

    if "type" in characteristics:
        output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_string(animals):
    """Generate HTML list items for all animals."""
    output = ""

    for animal in animals:
        output += serialize_animal(animal)

    return output


def write_html_file(file_path, content):
    """Writes the HTML content to a new file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    """Main entry point: generate animals.html from JSON data."""
    animals = load_data("data/animals_data.json")
    template = load_template("templates/animals_template.html")

    animals_string = generate_animals_string(animals)
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

    write_html_file("animals.html", final_html)


if __name__ == "__main__":
    main()
