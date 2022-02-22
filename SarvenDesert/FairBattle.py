# https://codecombat.com/play/level/fair-battle?
# Ataca cuando la energia total de tus soldados es mayor
# que la energia total de los ogros

# Esta funciona entrega la suma de la energia de las unidades.
def sumHealth(units):
    totalHealth = 0
    index = 0
    # Completa esta funcion:
    while index < len(units):
        unit = units[index]
        totalHealth += unit.health
        index += 1
    return totalHealth

while True:
    friends = hero.findFriends()
    enemies = hero.findEnemies()
    # Consigue la energia total de tus soldados y ogros.
    if sumHealth(friends) <= sumHealth(enemies):
        hero.say("Wait")
    # Di "Attack" cuando tengas mas energia total.
    else:
        hero.say("ATTACK!!!")