from time import sleep
from character.enemy.enemy import Bear
from encounters.encounters import standard_encounter
from story_module import StoryModule

class BearScenario(StoryModule):
	def executeModule(self, character):
		print "<You carry on along the dirt path towards the woods, night dawns soon.>"
		sleep(1)
		print
		print "<Thunder cracks heavily as you approach the woods, the glow of moonlight approaches and the sun bids its good byes. Best find some shelter>"
		sleep(1)
		print
		print "<You settle down in a nearby cave. This seems a good enough place to camp for the night>"
		sleep(1)
		print
		print "Bear: Grrrrr"
		print "<Oh No, a Wild Bear>"
		sleep(1)
		enemy = Bear()
		standard_encounter(character, enemy)
		print