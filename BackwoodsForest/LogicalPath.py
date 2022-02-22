# https://codecombat.com/play/level/logical-path?
# Obtené dos valores secretos true / false del mago.
# Consultá la guía para obtener notas sobre cómo escribir expresiones lógicas.
hero.moveXY(14, 24)
secretA = hero.findNearestFriend().getSecretA()
secretB = hero.findNearestFriend().getSecretB()

# Si tanto el secretoA como secretoB son verdaderos, tomá el camino alto; De lo contrario, tomar el camino bajo.
secretC = secretA and secretB
if secretC:
    hero.moveXY(20, 33)
else:
    hero.moveXY(20, 15)
hero.moveXY(26, 24)

# Si un secretoA o secretoB es verdadero, tomá el camino alto.
secretD = secretA or secretB
if secretD:
    hero.moveXY(32, 33)
else:
    hero.moveXY(32, 15)
hero.moveXY(38, 24)
# Si secretB no es verdadero, toma el camino alto.
secretE = not secretB
if secretE:
    hero.moveXY(44, 33)
else:
    hero.moveXY(44, 15)
hero.moveXY(50, 24)