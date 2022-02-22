# https://codecombat.com/play/level/munchkin-swarm?
while True:
    # Comprueba la distancia con tu enemigo mas cercano.
    nearestEnemy = hero.findNearestEnemy()
    distance = hero.distanceTo(nearestEnemy)
    # Si estas a 10 metros, desenfunda. 
    enemy = hero.findNearestEnemy()
    if distance < 10:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
    # Si no,ataca el "Cofre"
    else:
        hero.attack("Chest")
    pass