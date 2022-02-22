# https://codecombat.com/play/level/kithgard-brawl?
# Sobrevive las oleadas de ogros.
# Si ganas, el nivel se hace más difícil, y da mayores recompensas.
# Si pierdes, debes esperar un día para re-enviar.
# Cada vez que envías se generan nuevas condiciones aleatorias.
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    elif enemy:
        hero.attack(enemy)