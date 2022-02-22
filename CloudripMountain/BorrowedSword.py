# https://codecombat.com/play/level/borrowed-sword?
# En este nivel, tu heroe no pelea
# comanda a tus arqueros a enfocar su fuego en el enemigo con la mayor vida!

def commandTroops():
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'archer':
            CommandArcher(friend)


def CommandArcher(soldier):
    target = None
    leastHealth = 0
    enemyIndex = 0
    enemies = hero.findEnemies()

    while enemyIndex < len(enemies):
        if (enemies[enemyIndex].health > leastHealth):
            leastHealth = enemies[enemyIndex].health
            target = enemies[enemyIndex]
        enemyIndex = enemyIndex + 1
    if target:
        hero.command(soldier, "attack", target)


while True:
    commandTroops()