from classes import *

def execute():

def test_do_damage():
	#A Character and an enemy
	character = Character()
	enemy = Enemy()

	#Character has 3 attack and 5 health
	character.health = 5
	character.attack = 3

	#Enemy has 1 defense and 2 attack
	character.defense = 1
	character.attack = 2

	#Character does damage to enemy
	character.do_damage(enemy)

	
