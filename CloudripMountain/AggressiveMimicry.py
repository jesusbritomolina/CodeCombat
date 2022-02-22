# https://codecombat.com/play/level/aggressive-mimicry?
# Proteje la aldea de los ogros.
# Vigila a los ogros, campesinos y a los ogros disfrazados de campesinos.

# Esta función comprueba si el texto empieza con la palabra.
def startsWith(text, word):
    # Si la palabra es más larga entonces el texto:
    if len(word) > len(text):
        return False
    #  Bucle a través de los índices de la palabra y el texto.
    for index in range(len(word)):
        # Si los caracteres con el mismo índice son diferentes:
        if word[index] != text[index]:
            # Entonces la palabra no coincide con el texto.
            return False
    # Hemos verificado todas las letras y son iguales.
    return True

ogreNameStart = "Zog"

while True:
    suspectFriend = hero.findNearest(hero.findFriends())
    suspectName = suspectFriend.id
    # Use the function "startsWith" to check
    # Si el nombre (id) del sospechoso empieza con "Zog", atacar:
    if startsWith(suspectName, "Zog"):
        # Then attack suspectFriend:
        hero.attack(suspectFriend)
    enemy = hero.findNearestEnemy()
    # if there is an enemy, then attack it:
    if enemy:
        hero.attack(enemy)
    # De otra forma, volver a la marca roja con una X:
    else:
        hero.moveXY(27, 27)