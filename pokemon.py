from data import advantage_mult, health_mult, level_exp_dict, advantage_dict

class Pokemon():
  def __init__(self, name, type):
    self.name = name
    self.type = type
    self.level = 1
    self.exp = 0
    self.max_health = self.level * health_mult
    self.health = self.max_health
    self.k_o = False
  
  def __repr__(self):
    return "----------\n{name} ({type})\nLvl: {level}\nExp: {current_exp} / {goal_exp}\nHealth: {current_health} / {max_health}\n----------\n".format(
      name = self.name,
      type = self.type,
      level = self.level,
      current_exp = self.exp,
      goal_exp = level_exp_dict[self.level + 1],
      current_health = self.health,
      max_health = self.max_health
    )

  def calc_advantage(self, other_type):
    advantage = ""
    if other_type == advantage_dict[self.type]:
      advantage = "mine"
    elif self.type == advantage_dict[other_type]:
      advantage = "theirs"
    return advantage

  def attack(self, other, amount):
    advantage = self.calc_advantage(other.type)
    print("<< {name} attacks {other_name}! >>".format(
      name = self.name,
      other_name = other.name
    ))
    if advantage == "mine":
      amount = amount * advantage_mult
      print("<< It's super effective!! {amount} damage! >>".format(amount = amount))
      other.lose_health(amount)
    elif advantage == "theirs":
      amount = amount / advantage_mult
      print("<< It's not very effective... {amount} damage >>".format(amount = amount))
      other.lose_health(amount)
    else:
      print("<< {amount} damage >>".format(amount = amount))
      other.lose_health(amount)
    self.exp = self.exp + 1
    if self.exp >= level_exp_dict[self.level + 1]:
      self.level_up()

  def lose_health(self, amount):
    self.health = self.health - amount
    if self.health <= 0:
      self.health = 0
      self.knock_out()
      print(self)
    else:
      print("<< {name} lost {amount} health! >>\n".format(
        name = self.name,
        amount = amount
      ))
      print(self)

  def knock_out(self):
    if self.health == 0:
      self.k_o = True
    print("<< {name} was knocked out! >>\n".format(name = self.name))
  
  def gain_health(self, amount):
    self.health = self.health + amount
    if self.health > self.max_health:
      self.health = self.max_health
    print("<< {name} gained {amount} health! >>\n".format(
      name = self.name,
      amount = amount
    ))
    print(self)

  def revive(self):
    print("Reviving...")
    if self.k_o == True:
      self.health = 1
      print("<< {name} was revived! >>\n".format(name = self.name))
      print(self)
    else:
      print("<< {name} isn't knocked out. Why u do dis? >>".format(name = self.name))

  def full_revive(self):
    print("Full reviving...")
    self.revive()
    self.gain_health(self.max_health)

  def level_up(self):
    print("Leveling up!...")
    self.level = self.level + 1
    self.exp = self.exp - level_exp_dict[self.level]
    self.max_health = self.level * health_mult
    self.health = self.max_health
    print(self)