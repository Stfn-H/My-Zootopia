import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as file:
    return json.load(file)


def load_template(file_path):
    """Read and return the HTML template as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_animals_string(animals):
    """Generates the string with the animal data"""
    output = ""

    for animal in animals:
        output += '<li class="cards__item">\n'

        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"

        characteristics = animal.get("characteristics", {})

        if "diet" in characteristics:
            output += f"Diet: {characteristics['diet']}<br/>\n"

        locations = animal.get("locations", [])
        if locations:
            output += f"Location: {locations[0]}<br/>\n"

        if "type" in characteristics:
            output += f"Type: {characteristics['type']}<br/>\n"

        output += "</li>\n"

    return output


def write_html_file(file_path, content):
    """Writes the HTML content to a new file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    animals = load_data("data/animals_data.json")
    template = load_template("templates/animals_template.html")

    animals_string = generate_animals_string(animals)
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

    write_html_file("animals.html", final_html)


if __name__ == "__main__":
    main()
