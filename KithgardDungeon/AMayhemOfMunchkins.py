# https://codecombat.com/play/level/a-mayhem-of-munchkins?
# Inside a while-true loop, use findNearestEnemy() and attack!
while True:
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)