# https://codecombat.com/play/level/agrippa-refactored?
def cleaveOrAttack(enemy):
    # Si "cleave" está listo, usalo; si no, ataque.
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
    pass

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            # Usa la función "cleaveOrAttack", que definiste arriba.
            cleaveOrAttack(enemy)