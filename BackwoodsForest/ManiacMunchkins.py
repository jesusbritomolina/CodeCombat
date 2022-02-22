# https://codecombat.com/play/level/maniac-munchkins?
# ¡Otro cofre en el campo para que el héroe lo abra!
# Ataca el cofre para romperlo.
# ¡Algunos ogros no se quedarán de brazos cruzados mientras los atacas!
# Defiéndete cuando los ogros estén demasiado cerca.

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if hero.isReady("cleave"):
        # La primera prioridad es ver si cleave está listo:
        hero.cleave(enemy)
        pass
    elif distance < 5:
        # Ataca el ogro mas cercano si está demasiado cerca:
        hero.attack(enemy)
        pass
    else:
        # De lo contrario, intenta abrir el cofre:
        # Usa el nombre del cofre para atacar: "Chest".
        hero.attack("Chest")
        pass