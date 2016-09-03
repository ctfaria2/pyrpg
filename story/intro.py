from time import sleep
from character.hero.hero import *
from story_module import StoryModule

class Intro(StoryModule):
	def executeModule(self):
		print "Old Man: Welcome to PyPG, Please choose your class"

		while (True):
			for class_type in all_hero_classes():
				print "- " + class_type
			class_chosen = raw_input("Type that class that you want: ")
			print
			if (class_chosen not in all_hero_classes()):
				"Old Man: Please, choose an appropriate class"
			else:
				character = set_hero_class(class_chosen)
				break

		print "Old Man: You have chosen %s" % (class_chosen)
		print
		print "Old Man: Might i ask what your name is " + class_chosen + "?"
		name = raw_input("Type your name: ")

		character.name = name
		print "Old Man: Ahhh.. nice to meet you %s" % (character.name)
		sleep(0.7)
		print "Old Man: There is a sword. It is the finest sword ever created. Its being held by a group of Bandits in their camp in Restalt woods"
		sleep(1)
		print "Old Man: I have hired you %s so that you may fetch it for me. What do you say %s?" % (class_chosen, character.name)


		while (True):
			print
			choice = raw_input("Yes/No? ")
			if (choice == "No"):
				print
				print "Old Man: I guess another adventurer will come around"
				exit()
			elif (choice == "Yes"):
				print
				print "Old Man: Good.. good. I had hoped you would"
				break
			else:
				print
				print "Old Man: What did you say?"

		print "Old Man: Here takes this map. It will lead you to the woods. Good luck %s" % (character.name)
		sleep(2)
		print
		print "<Your adventure begins!>"
		sleep(2)
		print
		return character