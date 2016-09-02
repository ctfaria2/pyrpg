from sys import exit
from .attack import *
from .heal import *

actions = ["attack", "heal", "options"]

def standard_encounter(character, enemy):
	character.print_health()
	enemy.print_health()
	while (True):
		print
		print "<At any time, type 'options' to see the actions you are allowed>"
		print 
		action = raw_input("What do you want to do? ")
		print 

		if (action == "options"):
			for option in actions:
				print "- %s" %(option)
		elif (action.lower() == "attack"):
			success = attack(character, enemy)
			if success == True: break
		elif (action.lower() == "heal"):
			heal(character, enemy)