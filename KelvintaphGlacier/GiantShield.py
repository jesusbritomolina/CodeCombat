# https://codecombat.com/play/level/giant-shield?
# Use shieldBubble to extend your shield and get to Nalfar.

def CommandPaladin(paladin):
        hero.command(paladin, "move", {'x': 81, 'y': 45})

while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()
    
    for index, friend in enumerate(hero.findFriends()):
        if friend.type == 'paladin':
            CommandPaladin(friend)

    if flag:
        hero.pickUpFlag(flag)
        hero.shieldBubble()