# https://codecombat.com/play/level/match-cord?
# Ogres mined the field to protect their Chieftain.
# But we can use the "domino" effect get our target.
# The scout has prepared the map of the minefield.
# All mines are placed the same distance apart.
# The map is an array of strings, where "x" is a mine and "." is nothing.
# The first row in the array is the row nearest to the hero.

# The map and helpful constants are listed below.
fieldMap = hero.findFriends()[0].getMap()

mine = "x"
empty = "."
mineDistance = 5
firstXPos = 15
firstYPos = 40

# Find which starting mine connects to the ogre Chieftain.
map = []
i = 0
j = 0
for i in range(0, len(fieldMap)):
    map.push([])
for i in range(0, len(fieldMap)):
    for j in range(0, len(fieldMap[0])):
        if (fieldMap[i][j] == "x"):
            map[i].push("x")
        else:
            map[i].push(".")
hero.say(map[0].length + " nn " + map.length)


def find(arr, i, j):
    array = []
    array.push([i, j])
    while (len(array) > 0):
        temp = []
        for x in range(0, len(array)):
            m = array[x][0]
            n = array[x][1]
            arr[m][n] = "."
            if (n + 1 < 27 and arr[m][n + 1] == "x"):
                temp.push([m, n + 1])
                if (m == 15 and n + 1 == 13):
                    hero.moveXY(j * 5 + 15, 40)

            if (m + 1 < 16 and arr[m + 1][n] == "x"):
                temp.push([m + 1, n]);
                if (m + 1 == 15 and n == 13):
                    hero.moveXY(j * 5 + 15, 40)

            if (n - 1 >= 0 and arr[m][n - 1] == "x"):
                temp.push([m, n - 1])
                if (m == 15 and n - 1 == 13):
                    hero.moveXY(j * 5 + 15, 40);

            if (m - 1 >= 0 and arr[m - 1][n] == "x"):
                temp.push([m - 1, n])
                if (m - 1 == 15 and n == 13):
                    hero.moveXY(j * 5 + 15, 40)

        array = []
        array = temp


for j in range(0, len(map[0])):
    if (map[0][j] == "x"):
        find(map, 0, j)

resultColumn = 21 # ∆ Change this to your actual result!

hero.say("I think it's column number: " + resultColumn)
resultX = resultColumn * mineDistance + firstXPos
hero.moveXY(resultX, hero.pos.y)
hero.moveXY(resultX, firstYPos)