# https://codecombat.com/play/level/mountain-flower-grove?
# Este nivel es un lugar para hacer el arte de la flor.
# El verdadero objetivo es experimentar y divertirse!
# Si dibujas algo con un mínimo de 1.000 flores, tendrá "éxito" en el nivel.

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


for i in range(30, 120, 30):
    for j in range(30, 120, 30):
        color = colors[index % len(colors)]
        hero.setFlowerColor(color)
        index += 1
        drawCircle(i, j, 10)