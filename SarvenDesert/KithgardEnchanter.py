# https://codecombat.com/play/level/kithgard-enchanter?
# Define sus propias funciones de movimientos simples.
# Define moveRight
# Nota: cada función debe mover al héroe 12 metros!
def moveRight():
    x = hero.pos.x + 12
    y = hero.pos.y
    hero.moveXY(x, y)

# Define moveUp
def moveUp():
    x = hero.pos.x
    y = hero.pos.y + 12
    hero.moveXY(x, y)
# Define moveDown
def moveDown():
    x = hero.pos.x
    y = hero.pos.y - 12
    hero.moveXY(x, y)
# Ahora, use esas funciones!
moveRight()
moveDown()
moveUp()
moveUp()
moveRight()