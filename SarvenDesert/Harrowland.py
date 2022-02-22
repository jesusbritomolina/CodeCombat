# https://codecombat.com/play/level/harrowland?
# Use your cleverest programming tricks to outwit and overpower your opponent!
while True:
    enemy = None
    dist = 99999
    enemys = hero.findEnemies()
    index = 0
    while (index < len(enemys)):
        distance = hero.distanceTo(enemys[index])
        if (enemys[index].health > 0 and enemys[index].type != "sand-yak"):
            if (distance < dist):
                dist = distance
                enemy = enemys[index]
                index += 1
        if (enemy):
            if (hero.isReady("jump") and hero.distanceTo > 15):
                hero.jumpTo(enemy.pos)
            elif (hero.isReady("bash")):
                hero.bash(enemy)
            elif (hero.isReady("power-up")):
                hero.powerUp()
                hero.attack(enemy)
            elif (hero.isReady("cleave")):
                hero.cleave(enemy)
            else:
                hero.attack(enemy)