# https://codecombat.com/play/level/rational-defense?
# Protect the peasants.

# Move the peasants away from the woods.
def hideUnits(units):
    for i in range(len(units)):
        unit = units[i]
        hero.command(unit, "move", {'x': 34, 'y': 10 + i * 12})

# The peasants know the order in which to build the traps.
peasants = hero.findFriends()
buildOrder = peasants[0].buildOrder
separator = ","
# Split buildOrder with a comma (",")
# and save the result to the variable `types`:
types = buildOrder.split(separator)

# There are the same number of peasants as types.
for index in range(len(peasants)):
    peasant = peasants[index]
    x = 16
    y = 10 + index * 12
    # Get buildType by `index` from the array of types:
    buildType = types[index]
    # Command the peasant to buildXY the buildType at x and y:
    hero.command(peasant, 'buildXY', buildType, x, y)

# Watch for enemies and move peasants when ogres attack.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hideUnits(peasants)
        break

# Fight the ogres:
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)