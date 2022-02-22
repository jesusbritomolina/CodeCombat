# https://codecombat.com/play/level/cloudrip-treasure?
# Your goal is to collect coins / gems.
# This level is repeatable. If you win, the difficulty and rewards will increase.
# If you fail, you have to wait a day to resubmit.
# This level is an optional challenge level. You don't need to beat it to continue the campaign!
while True:
    enemy = hero.findNearestEnemy()
    
    flag = hero.findFlag()
    soldiers = hero.findFriends()
    item = hero.findNearestItem()
    
    for soldier in soldiers:
        if soldier and soldier.type == "peasant" and item:
            peasantItem =  soldier.findNearestItem()
            hero.command(soldier, "move", peasantItem.pos)
    
    for soldier in soldiers:
        if soldier and soldier.type == "soldier":
            hero.command(soldier, "defend", hero.pos)
            
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")
        
    elif enemy and hero.distanceTo(enemy) < 30:
        hero.attack(enemy)
        hero.moveXY(77, 60)