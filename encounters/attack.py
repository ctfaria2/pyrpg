from .death_handler import *

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