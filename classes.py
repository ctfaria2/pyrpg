from random import randint

class Character:
	name = ""
	health = 1
	max_health = 1
	attack = 1
	defense = 1
	luck = 1

	def do_damage(self, enemy, is_counter_attack = False):
		character_attack = randint(1, self.attack)
		character_attack += self.crit()
		if character_attack > enemy.defense:
			print "%s's attacks %s for %s damage" % (self.name, enemy.name, character_attack)
			enemy.health -= character_attack
		else:
			print "%s avoids the attack" % (enemy.name)

		if (enemy.is_alive() and is_counter_attack == False):
			enemy.counter_attack(self)

	def crit(self):
		crit_number = randint(0, 100)
		crit_damage = 0
		for i in range(1, self.luck):
			crit_chance = randint(0, 100)
			if (crit_number == crit_chance):
				print "Critical Hit! %s extra damage dealt" % (self.attack)
				crit_damage = self.attack
				break
		return crit_damage

	def counter_attack(self, enemy):
		self.do_damage(enemy, True)

	def heal(self):
		self.health += 3
		if (self.health >= self.max_health):
			self.health = self.max_health
		print "Healed for 3"

	def is_alive(self):
		return self.health > 0

	def print_health(self):
		print "%s is at %s health" % (self.name, self.health)


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


#Enemy Classes
class Enemy(Character):
	experience_dropped = 2

class Bandit(Enemy):
	def __init__(self):
		self.name = "Bandit"
		self.health = 10
		self.max_health = 10
		self.attack = 3
		self.defense = 1
		self.luck = 3
		self.experience_dropped = 3

class Bear(Enemy):
	def __init__(self):
		self.name = "Bear"
		self.health = 12
		self.max_health = 12
		self.attack = 3
		self.defense = 1
		self.luck = 2
		self.experience_dropped = 5

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