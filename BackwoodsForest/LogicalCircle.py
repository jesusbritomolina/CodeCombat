# https://codecombat.com/play/level/logical-circle?
# Move to the wizard and get their secret values.
hero.moveXY(20, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()
secretC = hero.findNearestFriend().getSecretC()

# If ALL three values are true, take the high path.
# Otherwise, take the low path. Save the 4th value.
secretD = secretA and secretB and secretC
if secretD:
    hero.moveXY(30, 33)
else:
    hero.moveXY(30, 15)

# If ANY of the three values are true, take the left path.
# Otherwise, go right. Save the 5th value.
secretE = secretA or secretB or secretC
if secretE:
    hero.moveXY(20, 24)
else:
    hero.moveXY(40, 24)
# If ALL five values are true, take the high path.
# Otherwise, take the low path.
if secretA and secretB and secretC and secretD and secretE:
    hero.moveXY(30, 33)
else:
    hero.moveXY(30, 15)