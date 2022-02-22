# https://codecombat.com/play/level/stranded-in-the-dunes?
# Go to the far right edge of the level to find new areas.
# Check the guide for more details.

while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    
    if flag:
        hero.pickUpFlag(flag)
    elif enemy and enemy.type != "sand-yak":
        hero.attack(enemy)