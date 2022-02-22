# https://codecombat.com/play/level/ring-bearer?
# You must escort a powerful magical ring back to town to be studied.
# The goal is to escape, not fight. More ogres lurk in the surrounding mountains!
# Make a circle of soldiers around the peasant!
# We give you two functions to help with this:

# findSoldierOffset figures out the position a soldier should stand at in relation to the peasant.
# The first argument 'soldiers' should be an array of your soldiers.
# The second argument 'i' is the index of the soldier (in soldiers) you want to find the position for.
def findSoldierOffset(soldiers, i):
    soldier = soldiers[i]
    angle = i * 360 / len(soldiers)
    return radialToCartesian(5, angle)

# This function does the math to determine the offset a soldier should stand at.
def radialToCartesian(radius, degrees):
    radians = Math.PI / 180 * degrees
    xOffset = radius * Math.cos(radians)
    yOffset = radius * Math.sin(radians)
    return {"x": xOffset, "y": yOffset}

peasant = hero.findByType("peasant")[0]

# Use findByType to get an array of your soldiers.
soldiers = hero.findByType("soldier")
while True:
    # Use a for-loop to iterate over range(len(soldiers)).
    friends = hero.findFriends()
    
    for i in range(len(soldiers)):
    # Find the offset for a soldier.
        offset = findSoldierOffset(soldiers, i)
    # Add the offset.x and offset.y to the peasant's pos.x and pos.y.
    # Command the soldier to move to the new offset position.
        hero.command(soldiers[i], "move", {'x':peasant.pos.x+offset.x,'y':peasant.pos.y+offset.y})
    # The hero should keep pace with the peasant!
    hero.move({"x": hero.pos.x + 0.2, "y": hero.pos.y})