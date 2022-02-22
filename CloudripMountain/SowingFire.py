# https://codecombat.com/play/level/sowing-fire?
# Goal: build three rows of nine fire-traps.

# Returns "retreat", "attack", "start-next-trap-column", or "build-next-trap-in-column"
def chooseStrategy():
    enemies = hero.findEnemies()
    
    # If there are overwhelming ogre forces, return the "retreat" strategy.
    if len(enemies) > 20:
        return "retreat"
    
    # If there are some ogres, return the "attack" strategy.
    if len(enemies) > 0:
        return "attack"
    # Use x % 9 is 0 to see if x is divisible by 9.
    # Use len(self.built) to see how many traps you have built.
    # If you have finished a column of 9 traps, return "start-next-trap-column"
    if len(self.built) % 9 == 0:
        return "start-next-trap-column"
    # Otherwise, return "build-next-trap-in-column"
    else:
        return "build-next-trap-in-column"

trapsInColumn = 9
startX = 40
columnX = startX

# Build the next trap in a column in the correct place.
def buildNextTrapInColumn(columnX,numTraps):
    # Change newY to use % to wrap around and only build trapsInColumn (9) traps per column
    newY = 7 * (numTraps % 9) + 10 # ∆ Change this to use % 9!
    if hero.pos.y < newY:
        hero.move({"x": columnX - 5, "y": newY})
    else:
        buildTrap(columnX,newY)

# Start a new column of traps.
def startNextTrapColumn(columnX, numTraps):
    newX = startX - (Math.floor(numTraps / trapsInColumn) * 6)
    if hero.pos.y > 10:
        hero.move({"x": newX - 5, "y": 10})
        return columnX
    else:
        buildTrap(newX,10)
        return newX

def buildTrap(x, y):
    hero.buildXY("fire-trap", x, y)

def commandAttack():
    # Have your griffin riders fend off the attackers.
    for friend in hero.findFriends():
        enemy = friend.findNearestEnemy()
        if enemy:
            hero.command(friend, 'attack', enemy)
    pass

def commandRetreat():
    hero.say("Retreat!")
    # You and your griffin riders retreat to safety behind the traps.
    hero.moveXY(4, 42)
    for friend in hero.findFriends():
        hero.command(friend, 'move', Vector(24, friend.pos.y))

while True:
    strategy = chooseStrategy()
    if strategy == "attack":
        commandAttack()
    elif strategy == "build-next-trap-in-column":
        buildNextTrapInColumn(columnX, len(hero.built))
    elif strategy == "start-next-trap-column":
        columnX = startNextTrapColumn(columnX, len(hero.built))
    elif strategy == "retreat":
        commandRetreat()