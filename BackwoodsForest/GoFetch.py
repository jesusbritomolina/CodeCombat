# https://codecombat.com/play/level/go-fetch?
# You've been caught in a burl trap!
# Send your pet to fetch the health potions!

def goFetch():
    # You can use loops in a handler function.
    while True:
        potion = hero.findNearestItem()
        if potion:
            # Use pet.fetch to fetch the potion.
            pet.fetch(potion)
            pass

# When your pet is summoned, it triggers a "spawn" event.
# This tells your pet to run the goFetch function at the start of the level:
pet.on("spawn", goFetch)