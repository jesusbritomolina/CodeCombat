# https://codecombat.com/play/level/grim-determination?
# http://codecombat.com/play/level/grim-determination
# Найти паладина с самым низким количеством здоровья.

def commandPaladin(paladin):
    if paladin.canCast("heal", paladin) and paladin.health < paladin.maxHealth:
        hero.command(paladin, "cast", "heal", paladin)
    else:
        target = paladin.findNearestEnemy()
        hero.command(paladin, "attack", target)
    pass


def commandPeasant(friend):
    item = friend.findNearestItem()
    if item:
        hero.command(friend, 'move', item.pos)


def commandGriffin(friend):
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy.type == "warlock":
            hero.command(friend, "attack", enemy)
        else:
            hero.command(friend, "attack", enemy)


def commandFriends():
    # Командуй своими союзниками.
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "peasant":
            commandPeasant(friend)
        elif friend.type == "griffin-rider":
            commandGriffin(friend)
        elif friend.type == "paladin":
            commandPaladin(friend)


while True:
    commandFriends()
    if hero.gold >= hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")