# https://codecombat.com/play/level/kithgard-apprentice?
# Tu objetivo es sobrevivir.
# También divertirse. Tal vez ganas en las tablas de clasificación!
# Lo bueno es que nunca se tropezó en esta habitación la primera vez que estuvo aquí, amirite?
# Your goal is to survive.
# Also have fun. Maybe win in the leaderboards!
# Good thing you never stumbled into this room the first time you were here, amirite?

def summon():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")

def command():
    targets = hero.findByType("soldier")
    for target in targets:
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.command(target, "attack", enemy)

witch = hero.findByType("witch")[0]

warlock = hero.findByType("warlock")[0]

while warlock.health > 0:
    hero.attack(warlock)

while witch.health > 0:
    hero.attack(witch)

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    summon()
    command()
    if flag:
        hero.pickUpFlag(flag)
    elif enemy and hero.distanceTo(enemy) < 5:
        hero.attack(enemy)