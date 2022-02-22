# https://codecombat.com/play/level/sacred-grove?
# Don’t let ogres step into the grove.

def onSpawn():
    while True:
        scout = pet.findNearestByType("scout")
        if scout and pet.isReady("charm"):
            pet.charm(scout)

# Assign the event handler to the pet's "spawn" event.
pet.on("spawn", onSpawn)
# Fight!
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)