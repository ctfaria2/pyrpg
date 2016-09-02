def heal(character, enemy):
	character.heal()
	enemy.counter_attack(character)
	if (handle_character_death(character, enemy) == True):
		exit()
	character.print_health()
	enemy.print_health()