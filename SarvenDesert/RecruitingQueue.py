# https://codecombat.com/play/level/recruiting-queue?
# Call peasants one after another.

# Neutral units are detected as enemies.
neutrals = hero.findEnemies()
while True:
    if len(neutrals):
        # Say the first unit in the neutrals array
        hero.say(neutrals[0])
        pass
    else:
        hero.say("Nobody here")
    
    # Reassign the neutrals variable using findEnemies()
    neutrals = hero.findEnemies()