# https://codecombat.com/play/level/skeleton-puzzle?
# Solve the puzzle and the treasures will be yours.
# Say numbers from 1 to 8 to move skeletons.

# The necromancer always knows the puzzle state.
boneMaster = hero.findFriends()[0]
puzzleState = boneMaster.getPuzzleState()
# The result state should be this:
goalState = [[1,2,3],[4,5,6],[7,8,0]]

# Solve, Solve, Solve!
def nearestDistanceFlag():
    enemies = hero.findEnemies()
    flag = hero.findFlag()
    for enemy in enemies:
        if flag:
            distance = flag.distanceTo(enemy)
            maxDistance = 10
            Distance = None
            skele = None
            if distance < maxDistance:
                Distance = distance
                skele = enemy
                hero.say(skele)
                
while True:
    nearestDistanceFlag()