from ..character import Character

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