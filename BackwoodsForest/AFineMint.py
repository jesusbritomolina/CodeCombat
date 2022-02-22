# https://codecombat.com/play/level/a-fine-mint?
# ¡Los peones están tratando de robar tus monedas!
# Escribe una función para aplastarlos antes de que puedan llevarse tus monedas.

def pickUpCoin():
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

# Escriba la función attackEnemy a continuación
# ¡Encuentra el enemigo más cercano y atácalo si existe!
def attackEnemy():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

while True:
    attackEnemy() # ∆ Descomente esta línea después de que escriba la función attackEnemy.
    pickUpCoin()