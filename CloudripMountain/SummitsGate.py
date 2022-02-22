# https://codecombat.com/play/level/summits-gate?
while True:
    paladins = []
    enemies = hero.findEnemies()
    if hero.canCast("invisibility", hero):
        hero.cast("invisibility", hero)
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == 'paladin':
            paladins.append(paladin)
    for enemy in enemies:
        if enemy.type == 'catapult':
            while enemy.health > 0:
                hero.attack(enemy)
        friends = hero.findFriends()
        for friend in friends:
            e = hero.findNearestEnemy()
            if e:
                hero.command(friend, "attack", e)
    fire = hero.findNearestEnemy()
    if fire:
        while fire.health > 0:
            hero.attack(fire)
        if fire.type == 'lower':
            pass
        fire = hero.findNearestEnemy()
        while fire.health > 0:
            hero.attack(fire)
        if hero.pos.x > 160:
            hero.moveXY(173, 34)
            hero.moveXY(173, 8)
            hero.moveXY(245, 14)
            hero.moveXY(245, 34)
            while hero.health < hero.maxHealth:
                hero.moveXY(245, 34)
                if hero.gold > hero.costOf("soldier"):
                    hero.summon("soldier")
                paladins = hero.findByType("paladin")
                for paladin in paladins:
                    if paladin:
                        if paladin.canCast("heal", paladin):
                            hero.command(paladin, "cast", "heal", hero)
            if hero.maxHealth == hero.health:
                if fire:
                    hero.moveXY(277, 34)
                    hero.moveXY(277, 5)
                    DJ = hero.findNearestEnemy()
                    if DJ:
                        while DJ.health > 0:
                            hero.attack(DJ)
                    hero.moveXY(277, 48)
                    lie = hero.findNearestEnemy()
                    if lie:
                        while lie.health > 0:
                            hero.attack(lie)
                    while True:
                        paladins = hero.findByType("paladin")
                        for paladin in paladins:
                            if paladin:
                                if paladin.canCast("heal", paladin):
                                    hero.command(paladin, "cast", "heal", hero)
                        fire = hero.findNearestEnemy()
                        if fire:
                            hero.attack(fire)