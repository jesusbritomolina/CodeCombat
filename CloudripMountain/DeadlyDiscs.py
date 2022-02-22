# https://codecombat.com/play/level/deadly-discs?
# If the ogre takes damage, she'll wake up and smash the peasant.
# You've got these razor-discs you can throw(). Maybe that'll help?
# Looks like you'll need three discs to defeat the ogre.
# Make all three hit the ogre simultaneously!
# Hint: razor discs bounce off of obstacles!

targets = []
targets.append({ "x": hero.pos.x, "y": hero.pos.y - 5 })
# Figure out where to throw the other two discs.
targets.append({ "x": hero.pos.x, "y": hero.pos.y + 5 })
targets.append({ "x": hero.pos.x - 1, "y": hero.pos.y})
while len(targets) > 0:
    if hero.isReady("throw"):
        # pop(0) removes and returns the first element of an array
        target = targets.pop(0)
        hero.throwPos(target)
    else:
        hero.wait(0.01)