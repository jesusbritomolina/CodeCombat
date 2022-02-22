# https://codecombat.com/play/level/reflective-shield?
# Use hero.reflect() to reflect back Nalfar's projectiles!

while True:
    missiles = hero.findEnemyMissiles()
    for missile in missiles:
        direction = Vector.subtract(missile.pos, hero.pos)
        if missile:
            hero.reflect(Vector(direction.x, direction.y, 1.9))