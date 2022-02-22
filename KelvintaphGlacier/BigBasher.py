# https://codecombat.com/play/level/big-basher?
# Use hero.slam() to deal AoE bash damage against enemies!

while True:
    enemy=hero.findNearestEnemy()
    if enemy:
        if hero.isReady("slam"):
            hero.slam(enemy)