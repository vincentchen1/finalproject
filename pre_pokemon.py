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


out_file = open('pokemon.json', 'w')
data = {}


add_trainer = input("Do you want to add a trainer? (yes/no) ")
if add_trainer == 'no':
    quit()
else:
    input_trainer_first_name = input("What is your first name? ")
    input_trainer_last_name = input("What is your last name? ")
    input_trainer_age = input("What is your age? ")
    input_trainer_ethnicity = input("What is your ethnicity? ")
    _trainer_pokemon = []
    trainer = Trainer(input_trainer_first_name, input_trainer_first_name, input_trainer_age, input_trainer_ethnicity,
                      _trainer_pokemon)
    print(TrainerEncoder().encode(trainer))
#    trainerJsonStr = json.dumps(trainer, indent=6, cls=TrainerEncoder)
#    json.dump(trainer, out_file, cls=TrainerEncoder)
    print()


while True:
    add_pokemon = input("Do you want to add a Pokemon? (yes/no) ")
    if add_pokemon == 'no':
        add_trainer = input("Do you want to add a trainer? (yes/no) ")
        if add_trainer == 'no':
            break
        else:
            input_trainer_first_name = input("What is your first name? ")
            input_trainer_last_name = input("What is your last name? ")
            input_trainer_age = input("What is your age? ")
            input_trainer_ethnicity = input("What is your ethnicity? ")
            _trainer_pokemon = []
            trainer = Trainer(input_trainer_first_name, input_trainer_first_name, input_trainer_age,
                              input_trainer_ethnicity, _trainer_pokemon)
            print(TrainerEncoder().encode(trainer))
            trainerJsonStr = json.dumps(trainer, indent=6, cls=TrainerEncoder)
            json.dump(trainer, out_file, cls=TrainerEncoder)
            print()

    else:
        input_name = input("What is your Pokemon's name? ")
        input_type = input("What is your Pokemon's type? ")
        input_level = input("What is your Pokemon's level? ")
        pokemon = Pokemon(input_name, input_type, input_level)
        print(PokemonEncoder().encode(pokemon))
        _trainer_pokemon = []
        trainer = Trainer(input_trainer_first_name, input_trainer_last_name, input_trainer_age, input_trainer_ethnicity,
                          _trainer_pokemon)
        _trainer_pokemon.append(pokemon)
        print(TrainerEncoder().encode(trainer))
        trainerJsonStr = json.dumps(trainer, indent=6, cls=TrainerEncoder)
        json.dump(trainer, out_file, cls=TrainerEncoder)
