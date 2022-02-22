# https://codecombat.com/play/level/reindeer-spotter?
# This array contains each of the pen's positions.
penPositions = [ {'x':20,'y':24}, {'x':28,'y':24}, {'x':36,'y':24}, {'x':44,'y':24}, {'x':52,'y':24} ]

# This array is used to track which reindeer is in it.
penOccupants = [ 'empty', 'empty', 'empty', 'empty', 'empty' ]

# And this array contains our reindeer.
friends = hero.findFriends()

# Figure out which reindeer are already in their pens.
for deerIndex in range(len(friends)):
    reindeer = friends[deerIndex]

    # Check each pen if it matches a reindeer's pos.
    for penIndex in range(len(penPositions)):
        penPos = penPositions[penIndex]

        if penPos.x == reindeer.pos.x and penPos.y == reindeer.pos.y:
            # Put the id in penOccupants at penIndex.
            penOccupants[penIndex] = reindeer.id
            # break out of the inner loop here.
            break;
            pass

# Tell Merek what's in each pen.
for occIndex in range(len(penOccupants)):
    # Tell Merek the pen index and the occupant.
    # Say something like "Pen 3 is Dasher"
    hero.say("Pen " + occIndex + " is " + penOccupants[occIndex])
    pass