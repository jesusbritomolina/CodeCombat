# https://codecombat.com/play/level/apocalypse?
# El apocalipsis artillería está sobre nosotros!
# Esquiva los proyectiles que se aproximan durante 60 segundos.
# Consejos: las banderas pueden ser útiles, como en Coinucopia.
# Debido a que los ataques son aleatorios cada vez que los envías, usted no puede moverse a su antojo con el codigo.

while True:
    flag = hero.findFlag()
    if (flag):
        if hero.distanceTo(flag) > 10 and hero.isReady('jump'):
            hero.jumpTo(flag.pos)
        else:
            hero.pickUpFlag(flag)
    else:
        hero.shield()