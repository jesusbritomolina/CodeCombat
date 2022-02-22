# https://codecombat.com/play/level/restless-dead?
# This level is supposed to be VERY hard! You may need a great strategy and or gear to complete it!

# Find and defeat the yeti then gather its essence for the ritual.
# You might want to gather the coins the yeti leaves behind, you'll need them to summon an army
# Stand at the summoning stone (red x) to begin summoning
# Now you just have to survive the undead hoard
while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    friends = hero.findFriends()
    
    if flag:
        hero.pickUpFlag(flag)
    elif hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    elif enemy:
        for friend in friends:
            hero.command(friend, "attack", enemy)
        if hero.isReady("cleave"):
            hero.cleave()
        else:
            hero.attack(enemy)