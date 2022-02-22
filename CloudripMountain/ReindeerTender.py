# https://codecombat.com/play/level/reindeer-tender?
# This is the array of pen positions
penPositions = [ {"x":20,"y":24}, {"x":28,"y":24}, {"x":36,"y":24}, {"x":44,"y":24}, {"x":52,"y":24} ]

# Use this array to keep track of each pen's reindeer.
penOccupants = [ None, None, None, None, None, ]

# And this array contains our reindeer.
friends = hero.findFriends()

# Figure out which reindeer are already in their pens.
for deerIndex in range(len(friends)):
    reindeer = friends[deerIndex]
    
    # For each position check if it matches a reindeer.
    for penIndex in range(len(penPositions)):
        penPos = penPositions[penIndex]
        
        if penPos.x == reindeer.pos.x and penPos.y == reindeer.pos.y:
            # Put the reindeer in occupants at penIndex
            penOccupants[penIndex] = penPositions[penIndex]
            # Remove the reindeer from the friends array.
            friends[deerIndex] = None
            # break out of the inner loop here:
            break
            pass

# Assign the remaining reindeer to new positions.
for deerIndex in range(len(friends)):
    # If the reindeer is null, use continue:
    if not friends[deerIndex]:
        continue
    reindeer = friends[deerIndex]
    
    # Look for the first pen with nothing.
    for occIndex in range(len(penOccupants)):
        # If there is nothing, the pen is open:
        if not penOccupants[occIndex]:
            # Put the reindeer in the occupants array.
            penOccupants[occIndex] = friends[deerIndex]
            # Command the reindeer to move to the pen.
            hero.command(penOccupants[occIndex], 'move', penPositions[occIndex])
            # break out early so we don't reassign:
            break
            pass