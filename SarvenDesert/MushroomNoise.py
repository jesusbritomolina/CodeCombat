# https://codecombat.com/play/level/mushroom-noise?
# Defeat the skeleton and open the chest.

def onSpawn (event):
    # Pet should find the health potion (type is "potion"): 
    potion = pet.findNearestByType("potion")
    # and fetch it:
    pet.fetch(potion)
    # Pet should find the gold key (type is "gold-key"):
    goldKey = pet.findNearestByType("gold-key")
    # and fetch it:
    pet.fetch(goldKey)
    pass

# Pet can find more than just items:
skeleton = pet.findNearestByType("skeleton")
pet.on("spawn", onSpawn)

while True:
    if skeleton.health > 0:
        hero.attack(skeleton)
    else:
        hero.moveXY(31, 38)