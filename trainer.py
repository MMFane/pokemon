class Trainer():
  def __init__(self, name, pokemon, num_potions, num_revives):
    self.name = name
    self.pokemon = *pokemon,
    self.active_pokemon = pokemon[0]
    self.num_potions = num_potions
    self.num_revives = num_revives

    if len(self.pokemon) > 6:
      # for index, pokemon in self.pokemon:
        # if index > 6:
        #   self.pokemon.remove(pokemon)
      print("<< you have too many pokemon\nputting {extras} back in the box >>".format(
        extras = "some pokemon"
      ))
      self.print_all_pokemon()

  def __repr__(self):
    return "--------------------\nHi, I'm {name}!\nI have {num} pokemon and I'm currently using {pokemon}\nInventory: {potions} potion(s), {revives} revive(s)\n--------------------\n".format(
      name = self.name,
      num = len(self.pokemon),
      pokemon = self.active_pokemon.name,
      potions = self.num_potions,
      revives = self.num_revives
    )

  def print_all_pokemon(self):
    for pokemon in self.pokemon:
      print(pokemon)