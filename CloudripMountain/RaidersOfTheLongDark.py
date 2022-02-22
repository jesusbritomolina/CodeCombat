# https://codecombat.com/play/level/raiders-of-the-long-dark?
# Your goal is to protect the peasant and move to the right.
# Arryn Stonewall will defend the front, and command the soldiers.
# You need to cover the rear and command the peasant.

arryn = hero.findByType("raider")[0]
peasant = hero.findByType("peasant")[0]

def chooseHeroStrategy():
    # Return either "fight" or "advance".
    # Try to stay 5m behind the peasant when not fighting.
    # Don't get more than 15m away from the peasant.
    enemy = peasant.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 5:
        return "fight"
    elif hero.distanceTo(peasant) < 15:
        return "advance"
    pass

def heroFight():
    # Stop the ogres from rushing past you to get to the peasant!
    # Hint: try to slow them down if you can
    enemy = peasant.findNearestEnemy()
    if enemy and hero.isReady("bash"):
        hero.bash(enemy)
    elif enemy:
        hero.attack(enemy)
    pass

def heroAdvance():
    # Stay behind the peasant
    hero.move(Vector(peasant.pos.x-5,peasant.pos.y))
    pass

def choosePeasantStrategy():
    # Return "follow", "build-above", or "build-below"
    # Hint: use isPathClear() to determine where the hallways are
    if hero.isPathClear(peasant.pos, Vector(peasant.pos.x, peasant.pos.y+10)):
        return "build-above"
    elif hero.isPathClear(peasant.pos, Vector(peasant.pos.x, peasant.pos.y-10)):
        return "build-below"
    else:
        return "follow"
    pass

def peasantAdvance():
    # Keep the peasant behind Arryn and her soldiers.
    hero.command(peasant, 'move', Vector(arryn.pos.x-5,arryn.pos.y))
    pass

def peasantBuild(x,y):
    # Command the peasant to build a palisade.
    hero.command(peasant, 'buildXY', 'palisade', x, y) 
    pass

while True:
    heroStrategy = chooseHeroStrategy()
    if heroStrategy == "fight":
        heroFight()
    elif heroStrategy == "advance":
        heroAdvance()
    
    peasantStrategy = choosePeasantStrategy()
    if peasantStrategy == "build-above":
        peasantBuild(peasant.pos.x, peasant.pos.y + 5)
    elif peasantStrategy == "build-below":
        peasantBuild(peasant.pos.x, peasant.pos.y - 5)
    elif peasantStrategy == "follow":
        peasantAdvance()