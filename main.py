from trainer import Trainer
from pokemon import Pokemon

# TEST BATTLE
pikachu = Pokemon("Pikachu", "electric")
bulbasaur = Pokemon("Bulbasaur", "grass")
squirtle = Pokemon("Squirtle", "water")
charmander = Pokemon("Charmander", "fire")
geodude = Pokemon("Geodude", "rock")
oddish = Pokemon("Oddish", "grass")
pichu = Pokemon("Pichu", "electric")

ash_pokemon = [pikachu, bulbasaur, squirtle, charmander, geodude, oddish, pichu]
ash = Trainer("Ash", ash_pokemon, 3, 1)
misty = Trainer("Misty", [squirtle], 1, 0)

# pikachu.attack(squirtle, 1)
# squirtle.attack(pikachu, 3)
# pikachu.attack(squirtle, 2)
# pikachu.attack(squirtle, 1)
# squirtle.attack(pikachu, 3)
# pikachu.attack(squirtle, 1)

print(ash)
print(misty)
