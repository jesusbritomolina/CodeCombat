# https://codecombat.com/play/level/kelvintaph-burgler?
# What eldritch artifacts are these? Don't let them blast you!
# The ice gate will open when both ogres are defeated.

while True:
    paladins = hero.findByType("paladin")
    friends = hero.findFriends()
    flag = hero.findFlag()
    if flag:
        hero.pickUpFlag(flag)
    for friend in friends:
        hero.command(friend, "move", {'x':12, 'y':57})
        hero.command(friend, "move", {'x':26, 'y':57})
        hero.command(friend, "move", {'x':30, 'y':52})
        hero.command(friend, "move", {'x':54, 'y':59})
        hero.command(friend, "move", {'x':76, 'y':57})
        hero.command(friend, "move", {'x':78, 'y':40})
        enemies = hero.findEnemies()
        for enemy in enemies:
            for paladin in paladins:
                if enemy.type == "witch":
                    hero.command(paladin, "attack", enemy)
                if enemy.type == "chieftain":
                    hero.command(paladin, "attack", enemy)
                for paladin in paladins:
                    if paladin:
                        if paladin.canCast("heal", paladin):
                            hero.command(paladin, "cast", "heal", friend)