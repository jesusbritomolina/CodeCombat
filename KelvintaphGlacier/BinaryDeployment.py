# https://codecombat.com/play/level/binary-deployment?
# Recruit soldiers and archers to fill out each squadron.
# Each paladin has a decimal number stored in her deployment attribute.
# Convert these to binary and represent them with lines of soldiers and archers next to each paladin.
# Soldiers are 0s, archers are 1s.
# For the bonus goal, add griffins as 2s for trinary number lines next to the warlocks.
# Check the guide for help with binary numbers.

units = ['soldier', 'archer', 'griffin-rider']

for i in range(len(hero.findFriends())):
    result = ""
    unit = hero.findFriends()[i]
    if unit.type == "paladin":
        divide = 2
    else:
        divide = 3
    number = unit.deployment
    while number >= divide:
        a = number % divide
        number = (number - a) / divide
        result = a + result
    result = number + result

    while len(result) < 8:
        result = '0' + result

    for k in range(len(result)):
        m = result[k]
        hero.summon(units[m])
        hero.command(hero.built[len(hero.built) - 1], "move", {'x': 14 + k * 6, 'y': unit.pos.y})