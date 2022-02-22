# https://codecombat.com/play/level/antipodes?
# El brujo usa el hechizo "clon" y creó antípodas del mal de nuestros arqueros .
# Pero incluso ese hechizo del mal tiene debilidades.
# Si tu arquero toca su antípoda, entonces desaparecerá.
# Si un arquero toca el clon equivocado o ataca a uno de ellos, entonces los clones empezaran a luchar .
# Podemos encontrar antípodas por sus nombres - que son inverso del otro.

# Esta acción comprueba si dos unidades son o no antípodas .
def areAntipodes(unit1, unit2):
    reversed1 = ""
    for i in range(len(unit1.id) - 1, -1, -1):
        reversed1 += unit1.id[i]
    return reversed1 == unit2.id

friends = hero.findFriends()
enemies = hero.findEnemies()

# Encuentra antípodas para cada uno de tus arqueros .
# Interatúa con todos los amigos
for friend in friends:
    # Para cada uno de los amigos iterar a todos los enemigos.
    for enemy in enemies:
        # Comprueba si el par de el actual amigo y el enemigo son antípodas .
        if areAntipodes(friend, enemy):
            # Si son antípodas , ordena al amigo a moverse hacia el enemigo 
            hero.command(friend, 'move', enemy.pos)

# Cuando todos los clones desaparezcan, ataca al brujo.
while True:
    targets = hero.findByType("archer")
    for target in targets:
        if target and target.team != "humans":
            hero.wait(1)
        else:
            enemy = hero.findNearestEnemy()
            if enemy:
                hero.attack(enemy)