# https://codecombat.com/play/level/first-out?
# Use queues to organize your soldiers and peasants.

units = hero.findFriends()
# This sergeant can enqueue and dequeue your units.
sergeant = hero.findByType("paladin", units)[0]
# The scout will help find enemies.
scout = hero.findByType("griffin-rider", units)[0]
soldiers = hero.findByType("soldier", units)
peasants = hero.findByType("peasant", units)

# First we need to prepare the soldiers:
for soldier in soldiers:
    # The sergeant can add a unit to the queue:
    sergeant.enqueue(soldier)
# Now "enqueue" the peasants:
for peasant in peasants:
    # The sergeant can command to enqueue an unit.
    sergeant.enqueue(peasant)

while True:
    enemy = scout.findNearestEnemy()
    # When enemies are here, dequeue the soldiers:
    if enemy:
        for s in soldiers:
            # Send soldiers with the "dequeue" method:
            sergeant.dequeue()
        break

while True:
    enemy = scout.findNearestEnemy()
    # If all the enemies are defeated:
    if not enemy:
        # "dequeue" the peasants:
        for s in peasants:
            sergeant.dequeue()
        break