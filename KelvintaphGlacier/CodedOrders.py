# https://codecombat.com/play/level/coded-orders?
# Read the message on the sign to determine which units to summon and where to place them.
# Check the guide for instructions on interpreting the orders.

sign = hero.findByType("sign")[0]
message = sign.message

# Tip: parse the sign, then summon the units, then send each unit to the right position.
summonTypes = {"a": "archer", "s": "soldier", "p": "peasant", "g": "griffin-rider", "P": "paladin", "A": "artillery"}
def summonTroops(num, coorX, coorY):
    type = summonTypes[num]
    if type != 'artillery' and hero.gold > hero.costOf(type):
        hero.summon(type)
    friends = hero.findByType(summonTypes[num], hero.findFriends())
    hero.command(friends[len(friends) - 1], 'move', {'x': int(coorX), 'y': int(coorY)})

sign = hero.findByType("sign")[0]
message = sign.message
for index in range(0, len(message), 5):
    type = message.substr(index, 1)
    x = message.substr(index + 1, 2)
    y = message.substr(index + 3, 2)
    summonTroops(type, x, y)