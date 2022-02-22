# https://codecombat.com/play/level/kelvintaph-pillars?
# Mueve la pila de campesinos a otro tocón.
# Sólo puedes llevar 1 campesino a la vez.
# No puedes apilar un campesino más grande sobre otro más pequeño.
# Tienes acceso a las siguientes APIs:
# pickUpItem(container) recoge el último elemento de un contenedor.
# dropItem(container) deja caer el último elemento de un contenedor.
# Los muñones tienen las siguientes APIs:
# peekItem() devuelve el elemento superior del contenedor.
# viewStack() devuelve un array de artículos en el contenedor.
# Los peones tienen las siguientes APIs:
# size; devuelve el tamaño del campesino

stump1 = hero.findByType("stump")[0] # Aquí comienzan los campesinos.
stump2 = hero.findByType("stump")[1]
stump3 = hero.findByType("stump")[2]

def move(frm, to):
    #hero.say(frm + '=>' + to)
    if frm == 2:
        hero.pickUpItem(stump1)
    elif frm == 1:
        hero.pickUpItem(stump2)
    else:
        hero.pickUpItem(stump3)

    if to == 2:
        hero.dropItem(stump1)
    elif to == 1:
        hero.dropItem(stump2)
    else:
        hero.dropItem(stump3)


def hanoi(n, frm, to, via):
    if (n == 1):
        move(frm, to)
        pass
    else:
        pass
        hanoi(n - 1, frm, via, to);
        move(frm, to)
        hanoi(n - 1, via, to, frm);


hanoi(5, 2, 3, 1)

#hero.pickUpItem(stump1)
#hero.dropItem(stump2)
#hero.say("Barrel 1 has the following peasants: " + stump1.viewStack())
#hero.say("Barrel 2's peasant is size: " + stump2.peekItem().size)