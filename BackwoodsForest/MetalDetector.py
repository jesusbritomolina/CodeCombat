# https://codecombat.com/play/level/metal-detector?
# The artillery uses coins as a target.
# You'll be the rangefinder for the artillery.

# Write the function.
def coinDistance():
    # Find the nearest coin,
    coin = hero.findNearestItem()
    # If there is a coin, return the distance to it.
    if coin:
        distance = hero.distanceTo(coin)
        return distance
    # Else, return 0 (zero).
    else:
        return 0
    pass

while True:
    distance = coinDistance()
    if distance > 0:
        # Say the `distance`.
        hero.say(distance)
        pass