# https://codecombat.com/play/level/kelvintaph-crusader?
def moveTo(position, fast=True):
    if (hero.isReady("jump") and fast):
        hero.jumpTo(position)
    else:
        hero.move(position)

def LowestFriend():
    lowestFriend = None
    lowestHealth = 99999
    friends = hero.findFriends()
    for friend in friends:
        if friend.health < friend.maxHealth and friend.health < lowestHealth:
            lowestFriend = friend
            lowestHealth = friend.health
            return lowestFriend

def CommandPaladin(paladin):
    if paladin.canCast("heal"):
        hero.command(paladin, "cast", "heal", LowestFriend())
    elif paladin.health < 200:
        hero.command(paladin, "shield")
    else:
        witches = hero.findByType("witch")
        for witch in witches:
            if witch:
                hero.command(paladin, "attack", witch)


if hero.canCast("chain-lightning", 'Trogdor'):
    hero.cast("chain-lightning", 'Trogdor')
    


def commandTroops():
    friends = hero.findFriends()
    paladins = hero.findByType("paladin")
    enemies = hero.findEnemies()
    witches = hero.findByType("witch")
    enemies = hero.findEnemies()
    ogre = hero.findByType("ogre", hero.findEnemies())
    for friend in friends:
        if friend.type != 'paladin':
            if ogre.health > 0:
                hero.command(friend, "attack", "Oni")
            elif ogre.health <= 0:
                if 'Rusty':
                    hero.command(friend, "attack", "Rusty")
                elif 'Skully':
                    hero.command(friend, "attack", "Skully")
        else:
            CommandPaladin(friend)

def EscapeTimeBoys():
    friends = hero.findFriends()
    for friend in friends:
        if hero.time > 22:
            hero.command(friend, "move", {'x': 32, 'y': 59})
            hero.command(friend, "move", {'x': 50, 'y': 57})
            hero.command(friend, "move", {'x': 50, 'y': 39})
        if hero.time > 30:
            hero.command(friend, "move", {'x': 78, 'y': 40})

def attack(target):
    if target:
        if (hero.distanceTo(target) > 10):
            moveTo(target.pos)
        elif (hero.isReady("bash")):
            hero.bash(target)
        else:
            hero.attack(target)

while True:
    commandTroops()
    EscapeTimeBoys()
    brawler = hero.findNearest(hero.findByType('brawler'))
    catapult = hero.findNearest(hero.findByType('catapult'))
    if brawler and hero.distanceTo(brawler) > 15:
        moveTo(brawler.pos, False)
    elif brawler:
        runaway = Vector.subtract(hero.pos, brawler.pos)
        runaway = Vector.normalize(runaway)
        runaway = Vector.multiply(runaway, 15)
        direction = Vector.add(runaway, hero.pos)
        moveTo(direction, False)
    elif catapult:
        attack(catapult)
    else:
        hero.move({'x': 78, 'y': 15})