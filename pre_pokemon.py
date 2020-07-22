import json
from json.encoder import JSONEncoder


class Pokemon:
    # def __init__(self):
    #     self.first_name = input("What is your first name? ")
    #     self.last_name = input("What is your last name? ")
    #     self.name = input("What is your Pokemon's name? ")
    #     self.poke_type = input("What is your Pokemon's type? ")
    #     self.level = input("What is your Pokemon's level? ")

    def __init__(self, _first_name, _last_name, _name, _type, _level):
        self.first_name = _first_name
        self.last_name = _last_name
        self.name = _name
        self.type = _type
        self.level = _level


# subclass JSONEncoder
class PokemonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


out_file = open('pokemon.json', 'w')

while True:

    start = input("Do you want to add a trainer? yes/no ")
    if start == 'yes':
        input_first_name = input("What is your first name? ")
        input_last_name = input("What is your last name? ")
        input_name = input("What is your Pokemon's name? ")
        input_type = input("What is your Pokemon's type? ")
        input_level = input("What is your Pokemon's level? ")
        pokemon = Pokemon(input_first_name, input_last_name, input_name, input_type, input_level)
        print(PokemonEncoder().encode(pokemon))
        pokemonJsonStr = json.dumps(pokemon, indent=6, cls=PokemonEncoder)
        json.dump(pokemon, out_file, cls=PokemonEncoder)
        print()
    else:
        quit()
