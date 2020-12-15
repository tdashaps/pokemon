import os

class Game:
    def __init__(self, playerName, rivalName):
        self.player
        self.stopped = True
    def start():
        while self.stopped == False:

class Trainer:
    def _init__(self, title, name, element, team: Team):
        pass

class Team(list):
    def __init__(self, pokedex: PokeDex, *pokemon_names):
        super().__init__()
        for name in pokemon_names:
            pokemon = Pokemon(name)
            self.append(pokemon)

class Pokemon:
    def __init__(self, name, pokemon):
        self.raw_json = Pokemon.get_all()
        
    @staticmethod
    def get_all():
        with open(os.path.join(os.getcwd(), "pokemon.json"), 'r+') as pokemon:
            return json.loads(pokemon)
