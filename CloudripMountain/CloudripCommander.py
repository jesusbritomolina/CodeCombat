# https://codecombat.com/play/level/cloudrip-commander?
# Summon some soldiers, then direct them to your base.

# Each soldier costs 20 gold.
while hero.gold > hero.costOf("soldier"):
    hero.summon("soldier")
    
soldiers = hero.findFriends()
soldierIndex = 0
# Add a while loop to command all the soldiers.
while soldierIndex < len(soldiers):
    
    soldier = soldiers[soldierIndex]
    hero.command(soldier, "move", {"x": 50, "y": 40})
    soldierIndex += 1
    # Go join your comrades!

while soldierIndex == len(soldiers):
    hero.moveXY(50, 40)