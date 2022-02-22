# https://codecombat.com/play/level/airbender?
# Use hero.forcePush() to push skeletons into fire-traps.

while True:
    skel = hero.findNearest(hero.findByType('skeleton'))
    enemy = hero.findNearestEnemy()
    direction = Vector.normalize(Vector.subtract(enemy.pos, hero.pos))
    if skel and hero.isReady('force-push'):
        hero.forcePush(skel, direction, 0.4)