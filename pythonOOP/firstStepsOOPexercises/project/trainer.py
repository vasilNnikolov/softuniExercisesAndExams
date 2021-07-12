from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [p.name for p in self.pokemons]
        if pokemon_name in pokemon_names:
            pokemon_to_release_index = pokemon_names.index(pokemon_name)
            self.pokemons.pop(pokemon_to_release_index)
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        data_as_list = []
        data_as_list.append(f"Pokemon Trainer {self.name}")
        data_as_list.append(f"Pokemon count {len(self.pokemons)}")
        for p in self.pokemons:
            data_as_list.append(f"- {p.pokemon_details()}")

        return "\n".join(data_as_list)
