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