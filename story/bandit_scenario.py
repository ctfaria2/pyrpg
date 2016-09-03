from time import sleep
from character.enemy.enemy import Bandit
from encounters.encounters import standard_encounter
from story_module import StoryModule

class BanditScenario(StoryModule):
	def executeModule(self, character):
		print "<You set out from the village of Werchter via the North gate. According to the Old Man's map, this will lead you to the forest>"
		sleep(2)
		print 
		print "<Along the way you are attacked by a Bandit!>"
		sleep(1)
		enemy = Bandit()
		standard_encounter(character, enemy)
		print