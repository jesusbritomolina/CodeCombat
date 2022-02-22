# https://codecombat.com/play/level/the-trials?
# Este nivel está destinado a ser para jugadores avanzados. La solución debe ser bastante compleja con un montón de piezas móviles. También podría ser un poco de un control de engranajes a menos que utilice métodos "creativos".
# Necesitás hacer tu camino a la primera prueba (Oasis de Marr) derrotando a los enemigos en el camino. Cuando llegues a él, recoge todas las setas para iniciar la prueba. Si sobrevives a la embestida, hazte camino al siguiente Oasis para el segundo juicio, luego al Templo. Cuando todos los juicios estén completos tendrá que enfrentar al jefe final. ¡Buena suerte!
# SUGERENCIA: Las gafas con un alto rango visual ayudan enormemente en este nivel, así que compra lo mejor que puedes conseguir.
# SUGERENCIA: la unidad 'tipo' para los guardianes de oasis es 'oasis-guardian'

array = [[31, 26], [53, 21], [74, 21], [86, 21], [112, 23], [127, 25], [68, 20], [51, 25], [12, 53], [10, 86],
         [16, 115], [34, 126], [12, 112], [34, 126], [12, 112], [34, 126], [12, 112], [34, 126], [12, 112], [34, 126],
         [12, 112], [44, 130], [60, 125], [85, 32], [103, 125], [85, 32], [103, 125], [85, 32], [103, 125], [85, 32],
         [103, 125], [41, 95], [40, 84], [100, 89], [130, 72], [102, 55]]
arrayIndex = 0;
while arrayIndex < len(array):
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if (enemy and hero.distanceTo(enemy) < 50):
        if (hero.isReady('jump') and hero.distanceTo(enemy) > 10):
            hero.jumpTo(enemy.pos)
        elif (hero.isReady("cleave")):
            hero.cleave(enemy)
        elif (hero.isReady("bash")):
            hero.bash(enemy)
        elif (hero.isReady("power-up")):
            hero.powerUp()
            hero.attack(enemy)
        else:
            hero.attack(enemy)
    elif (item):
        if (hero.isReady('jump')):
            hero.jumpTo(item.pos)
        else:
            hero.moveXY(item.pos.x, item.pos.y)
    else:
        if (hero.isReady('jump')):
            hero.jumpTo({'x': array[arrayIndex][0], 'y': array[arrayIndex][1]})
        else:
            hero.moveXY(array[arrayIndex][0], array[arrayIndex][1])
        arrayIndex += 1