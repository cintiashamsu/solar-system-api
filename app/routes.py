from flask import Blueprint, jsonify

# 1. Define a `Planet` class with the attributes `id`, `name`, and `description`, and one additional attribute
# 1. Create a list of `Planet` instances
class Planet:
    def __init__(self, id, name, description, rings):
        self.id = id
        self.name = name
        self.description = description
        self.rings = rings

PLANETS = [
    Planet(1, 'Earth', 'home planet', 0),
    Planet(2, 'Saturn', '6th planet from the sun', 7),
    Planet(3, 'Jupiter', '5th planet', 4)
]

planets_bp = Blueprint('planets_bp', __name__, url_prefix='/planets')

@planets_bp.route('', methods=['GET'])
def get_all_planets():
    planet_response = []
    for planet in PLANETS:
        planet_response.append({
            'id': planet.id,
            'name': planet.name,
            'description': planet.description,
            'rings': planet.rings
        })

    return jsonify(planet_response)