# https://codecombat.com/play/level/agrippa-returned?
def enemyInRange(enemy):
    # Devuelve verdadero si el enemigo esta a menos de 5 unidades.
    distance = hero.distanceTo(enemy)
    if distance < 5:
        return True
    else:
        return False

def cleaveOrAttack(enemy):
    if hero.isReady('cleave'):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Verifica la distancia del enemigo llamando enemyInRange(enemigoEnRango).
        if enemyInRange(enemy):
            cleaveOrAttack(enemy)