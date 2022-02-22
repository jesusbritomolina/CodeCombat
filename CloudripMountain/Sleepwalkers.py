# https://codecombat.com/play/level/sleepwalkers?
# Nuestros campesinos sonámbulos están regresando.
# But sleeping yetis are also coming.
# ¡NO LOS DESPIERTES!
# Construye vallas para detener a los yetis y que los campesinos puedan pasar.


# Senick preparó un mapa cuadriculado de cómo construir vallas.
hunter = hero.findNearest(hero.findFriends())
fenceMap = hunter.getMap()

# Esta función convierte el mapa en coordenadas XY.
def convertCoor(row, col):
    return {'x': 34 + col * 4, 'y': 26 + row * 4}


# Repite sobre fenceMap y construye en la cerca en todos los 1.
for ri, row in enumerate(fenceMap):
    for rx, col in enumerate(row):
        if (col == 1):
            coor = convertCoor(ri, rx)
            hero.buildXY('fence', coor.x, coor.y)

# Regresa a la villa después de construir las vallas.
hero.moveXY(22, 15)