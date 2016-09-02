from character import *
from sys import exit

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
			print "- attack"
			print "- heal"
			print "- options"
		elif (action == "attack"):
			success = attack(character, enemy)
			if success == True: break
		elif (action == "heal"):
			heal(character, enemy)
			

def attack(character, enemy):
	character.do_damage(enemy)
	if (handle_enemy_death(enemy) == True):
		character.gain_exp(enemy.experience_dropped)
		return True
	elif (handle_character_death(character, enemy) == True):
		exit()
	character.print_health()
	enemy.print_health()
	return False

def heal(character, enemy):
	character.heal()
	enemy.counter_attack(character)
	if (handle_character_death(character, enemy) == True):
		exit()
	character.print_health()
	enemy.print_health()

def handle_enemy_death(enemy):
	is_dead = False
	if (enemy.is_alive() != True):
		print 
		print "<%s dies>" % (enemy.name)
		is_dead = True
	return is_dead

def handle_character_death(character, enemy):
	is_dead = False
	if (character.is_alive() != True):
		print
		print "<You have failed %s you have been slain by %s>" % (character.name, enemy.name)
		is_dead = True
	return is_dead
