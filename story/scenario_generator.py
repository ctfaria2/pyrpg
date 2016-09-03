from random import randint
from sys import exit

from .bandit_scenario import BanditScenario
from .bear_scenario import BearScenario

class ScenarioGenerator:

	def generate(self, character):
		random = randint(0, 100)
		if ((random % 2) == 0):
			BearScenario().executeModule(character)
		else:
			BanditScenario().executeModule(character)

		if (random > 75):
			exit()
		else:
			self.generate(character)