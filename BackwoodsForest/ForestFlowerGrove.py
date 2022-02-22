# https://codecombat.com/play/level/forest-flower-grove?
# This level is a place for making flower art.
# The real goal is to experiment and have fun!
# If you draw something with at least 1000 flowers, you will *succeed* at the level.
colors = ["pink", "red", "blue", "purple", "yellow", "white", "random"]
index = len(colors)


def drawCircle(x, y, size):
    angle = 0
    hero.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)
        angle += 0.2


for i in range(30, 120, 10):
    for j in range(30, 120, 10):
        color = colors[index % len(colors)]
        hero.setFlowerColor(color)
        index += 1
        drawCircle(i, j, 5)