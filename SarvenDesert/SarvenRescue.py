# https://codecombat.com/play/level/sarven-rescue?
# Rescata a la campesina de los bandidos y devuélvela al pueblo.
# Elige el camino que más te convenga, evitando las patrullas o enfrentándote a ellas de frente.
# Las pociones otorgarán efectos aleatorios, algunos buenos y otros malos.
# ¿Te sientes valiente? Bonificación si puedes saquear el cofre del tesoro del ogro.

while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        hero.pickUpFlag(flag)
    elif enemy:
        hero.attack(enemy)