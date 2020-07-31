import json
from json.encoder import JSONEncoder


class Pokemon:
    # def __init__(self):
    #     self.first_name = input("What is your first name? ")
    #     self.last_name = input("What is your last name? ")
    #     self.name = input("What is your Pokemon's name? ")
    #     self.poke_type = input("What is your Pokemon's type? ")
    #     self.level = input("What is your Pokemon's level? ")

    def __init__(self, _name, _type, _level):
        self.name = _name
        self.type = _type
        self.level = _level


class Trainer:
    def __init__(self, _trainer_first_name, _trainer_last_name, _trainer_age, _trainer_ethnicity, _trainer_pokemon):
        self.first_name = _trainer_first_name
        self.last_name = _trainer_last_name
        self.age = _trainer_age
        self.ethnicity = _trainer_ethnicity
        self.pokemon = _trainer_pokemon


# subclass JSONEncoder
class PokemonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class TrainerEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


# a file is created that allows you to write over a JSON file
out_file = open('pokemon.json', 'w')

# two lists are used that allows the storage of created trainers and Pokemon
_trainers = []
_trainer_pokemon = []
while True:
    # Ask for trainer information
    add_trainer = input("Do you want to add a trainer? (yes/no) ")
    if add_trainer == 'no':
        break
    else:
        input_trainer_first_name = input("What is your first name? ")
        input_trainer_last_name = input("What is your last name? ")
        input_trainer_age = input("What is your age? ")
        input_trainer_ethnicity = input("What is your ethnicity? ")

# this list is restarted and then now used to collect Pokemon information
    _trainer_pokemon = []
#
    while True:
        add_pokemon = input("Do you want to add a Pokemon? (yes/no) ")
        if add_pokemon == 'no':
            break
        else:
            input_name = input("What is your Pokemon's name? ")
            input_type = input("What is your Pokemon's type? ")
            input_level = input("What is your Pokemon's level? ")
            pokemon = Pokemon(input_name, input_type, input_level)
            _trainer_pokemon.append(pokemon)

# all this information, trainer and Pokemon is kept as a class object
    trainer = Trainer(input_trainer_first_name, input_trainer_last_name, input_trainer_age,
                      input_trainer_ethnicity, _trainer_pokemon)
# the multiple objects are then stored within the _trainers list
    _trainers.append(trainer)


# trainerJsonStr = json.dumps(_trainers, indent=6, cls=TrainerEncoder)
# all the stored data is then dumped inside pokemon.JSON and sorted via key-value in alphabetical order
json.dump(_trainers, out_file, indent=4, sort_keys=True, cls=TrainerEncoder)
