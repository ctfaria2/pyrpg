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