from flask import Blueprint, jsonify, abort, make_response

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
    planet_response = [vars(planet) for planet in PLANETS]
    return jsonify(planet_response)

# GET ONE PLANET
@planets_bp.route('/<id>', methods=['GET'])
def get_one_planet(id):
    planet = validate_planet(id)
    return planet
    
# VALIDATION FUNCTION
def validate_planet(id):
    # handle invalid data types such as non-ints
    try:
        planet_id = int(id)
    except ValueError:
        return{
            "message": "Invalid planet id"
        }, 400
    
    # handle if id not found
    for planet in PLANETS:
        if planet.id == planet_id:
            return vars(planet)
        
    abort(make_response(jsonify(description="Resource not found"),404))