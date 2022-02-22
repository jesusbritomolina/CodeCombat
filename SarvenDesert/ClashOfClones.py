# https://codecombat.com/play/level/clash-of-clones?
# ¡Necesitarás una buena estrategia y un buen equipo para ganar esta batalla!
# ¡Tu clon va a tener el mismo equipo que tienes!
# Pero, no tienen buenas habilidades con poderes especiales.

enemy = hero.findNearestEnemy()

hero.cast("chain-lightning", enemy)

while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    if flag:
        hero.pickUpFlag(flag)
    elif enemy and enemy.type != "sand-yak":
        if hero.isReady("bash") and enemy.health < 116:
            hero.bash(enemy)
        else:
            hero.attack(enemy)