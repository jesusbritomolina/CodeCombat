# https://codecombat.com/play/level/square-shield?
# Incoming yeti attack! Use your paladins to form a square!

def findByName(name, thangs):
    for i in range(len(thangs)):
        thang = thangs[i]
        if thang.id == name:
            return thang
    return None
friends = hero.findFriends()
# Celadia is in the top left corner.
celadia = findByName("Celadia", friends)
# Dedalia is in the top right corner.
dedalia = findByName("Dedalia", friends)
sideLength = celadia.distanceTo(dedalia)

# Illumina and Vaelia should finish forming a square!
vaelia = findByName("Vaelia", friends)
illumina = findByName("Illumina", friends)

# Command Vaelia to move to the bottom left corner of the square.
hero.command(vaelia, 'move', {'x': dedalia.pos.x, 'y': dedalia.pos.y - sideLength})
# Command Illumina to move to the bottom left corner of the square.
hero.command(illumina, 'move', {'x': celadia.pos.x, 'y': celadia.pos.y - sideLength})