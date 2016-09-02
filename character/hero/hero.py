from ..character import Character

# Hero Classes
class Hero(Character):
	experience = 0
	level_limit = 10

	def gain_exp(self, exp):
		self.experience += exp
		print "%s has gained %s exp." % (self.name, exp)
		print "%s exp until the next level" % ((self.level_limit - self.experience))
		if (self.experience >= self.level_limit):
			print "%s has leveled up" % (self.name)
			self.experience = self.experience - self.level_limit
			self.level_limit = self.level_limit * 2
			self.level_up()

	def level_up(self):
		self.max_health += 2
		self.health = self.max_health
		self.attack += 2
		self.defense += 2
		self.luck += 1

class Warrior(Hero):
	def __init__(self):
		self.health = 4
		self.max_health = 4
		self.attack = 4
		self.defense = 2
		self.luck = 1
		#11

	def level_up(self):
		self.max_health += 2
		self.health = self.max_health
		self.attack += 3
		self.defense += 1
		self.luck += 1

class Mage(Hero):
	def __init__(self):
		self.health = 6
		self.max_health = 6
		self.attack = 3
		self.defense = 1
		self.luck = 1
		#11

class Thief(Hero):
	def __init__(self):
		self.health = 4
		self.max_health = 4
		self.attack = 3
		self.defense = 2
		self.luck = 2
		#11

	def level_up(self):
		self.max_health += 2
		self.health = self.max_health
		self.attack += 2
		self.defense += 1
		self.luck += 2

class Brute(Hero):
	def __init__(self):
		self.health = 5
		self.max_health = 5
		self.attack = 2
		self.defense = 3
		self.luck = 1
		#11

	def level_up(self):
		self.max_health += 2
		self.health = self.max_health
		self.attack += 1
		self.defense += 3
		self.luck += 1


class Priest(Hero):
	def __init__(self):
		self.health = 7
		self.max_health = 7
		self.attack = 2
		self.defense = 1
		self.luck = 1
		#11

	def heal(self):
		self.health += 5
		if (self.health > self.max_health):
			self.heal = self.max_health
		print "Healed for 5"

	def level_up(self):
		self.max_health += 3
		self.health = self.max_health
		self.attack += 2
		self.defense += 1
		self.luck += 1

# Class Code
hero_classes = {
	"Warrior" : Warrior(),
	"Mage" : Mage(),
	"Thief" : Thief(),
	"Brute" : Brute(),
	"Priest" : Priest()
}

def all_hero_classes():
	return hero_classes.keys()

def set_hero_class(hero_class):
	return hero_classes[hero_class]