# https://codecombat.com/play/level/sarven-sum?
# To disable the fire-traps add the lowest trap.value to the highest value.
# Para desactivar las fire-traps añade el más bajo trap.value al valor más alto.
# Muévete a la X blanca y di la respuesta a Kitty el puma.
# Derrota a todos los ogros si te atreves.
# Una vez derrotados todos los ogros muévete a la X roja.
# Busca pociones para aumentar tu salud.

whiteX = {'x':27, 'y':42}
redX = {'x':151 , 'y': 118}

def drinkPotion(item):
    item = hero.findNearestItem()
    if item and item.type != "poison":
    	hero.moveXY(item.pos.x, item.pos.y)

max = 0
min = 999
hazards = hero.findHazards()
pointIndex = 0
while pointIndex < len(hazards):
    hazard = hazards[pointIndex]
    if hazard.value < min:
    	min = hazard.value
    if hazard.value > max:
    	max = hazard.value
    pointIndex += 1
hero.moveXY(27, 42)
hero.say(min+max)
pointIndex = 0

while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    flag = hero.findFlag()
    
    if enemy:
        hero.attack(enemy)
    elif item:
        drinkPotion(item)
    else:
        if flag:
            hero.pickUpFlag(flag)
        pointIndex += 1
        continue