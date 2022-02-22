# https://codecombat.com/play/level/dueling-grounds?
# Defeat the enemy hero in a duel!

while True:
    # Find and attack the enemy inside a loop.
    # When you're done, submit to the multiplayer ladder!
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)