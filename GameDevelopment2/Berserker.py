# https://codecombat.com/play/level/berserker?
# Mushrooms allow the player to destroy fences for a time.

player = game.spawnPlayerXY('captain', 12, 34)
player.maxSpeed = 15
game.addMoveGoalXY(76, 34)
ui.track(game, "time")

# The duration of the mushroom power.
game.powerDuration = 3
# The time the mushroom power expires at.
game.powerEndTime = 0

# "mushroom"s are collectable items without default effects.
game.spawnXY("mushroom", 12, 52)
game.spawnXY("mushroom", 12, 16)
game.spawnXY("mushroom", 36, 16)
game.spawnXY("mushroom", 36, 52)
game.spawnXY("mushroom", 56, 12)
game.spawnXY("mushroom", 56, 56)
game.spawnXY("mushroom", 56, 34)

# The event handler for "collect" events.
def onCollect(event):
    unit = event.target
    item = event.other
    if item.type == "mushroom":
        # "scale" changes the visual size of the unit.
        unit.scale = 2
        game.powerEndTime = game.time + game.powerDuration
        unit.say("ARRRGH!!!")

# The event handler for "collide" events.
def onCollide(event):
    # The event owner who has collided with something.
    unit = event.target
    # The object the unit collided with.
    collidedObject = event.other
    # If it's a fence.
    if collidedObject.type == "fence":
        if unit.scale == 2:
            # Use the `destroy` method of collidedObject.
            collidedObject.destroy()
            pass

# Assign onCollide to the "collide" event on the player.
player.on("collide", onCollide)
# Assign onCollect to the "collect" event on the player.
player.on("collect", onCollect)

def checkTimers():
    # If game time is greater than game.powerEndTime:
    if game.time > game.powerEndTime:
        # If player.scale is equal to 2: 
        if player.scale == 2:
            # Set the player's scale to 1.
            player.scale = 1
    pass

while True:
    checkTimers()