# https://codecombat.com/play/level/what-in-carnation?
twoPi = 2 * Math.PI

# Here are some functions for drawing shapes:
def degreesToRadians(degrees):
    return (degrees/360)*twoPi

def drawPolyStars(center, radius, sides, skips, startAngle):
    angle = startAngle
    x = center.x
    y = center.y
    hero.toggleFlowers(False)
    loops = skips + 1
    stepAngle = loops * (twoPi / sides)
    if skips != 0 and (sides % loops) == 0:
        loops = skips
    endAngle = (twoPi * loops) + startAngle
    while angle <= endAngle:
        newX = x + radius * Math.cos(angle)
        newY = y + radius * Math.sin(angle)
        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)
        angle += stepAngle

def drawStar(center, radius, sides, skips, startAngle):
    skipsPlusOne = skips + 1
    if ((sides/skipsPlusOne) != 1 and (sides%skipsPlusOne) == 0):
        for index in range(skipsPlusOne):
            angle = startAngle + index * (twoPi / sides)
            drawPolyStars(center, radius, sides, skips, angle)
    else:
        drawPolyStars(center, radius, sides, skips, startAngle)

def drawPolygon(center, radius, sides, startAngle):
    drawPolyStars(center, radius, sides, 0, startAngle)

def drawSpokes(center, radius, sides, startAngle):
    x = center.x
    y = center.y
    endAngle = twoPi + startAngle
    stepAngle = twoPi / sides
    angle = startAngle
    while angle < endAngle:
        newX = x + radius * Math.cos(angle)
        newY = y + radius * Math.sin(angle)
        if int(hero.pos.x) == int(x) and int(hero.pos.y) == int(y):
            hero.toggleFlowers(True)
            hero.moveXY(newX, newY)
        else:
            hero.toggleFlowers(False)
            hero.moveXY(newX, newY)
            hero.toggleFlowers(True)
            hero.moveXY(x, y)
        hero.toggleFlowers(False)
        angle += stepAngle

def ternary(thisOne, condition, thatOne):
    if condition:
        return thisOne
    else:
        return thatOne

def drawSpiral(center, size, loopNum, startAngle):
    x = center.x
    y = center.y
    hero.toggleFlowers(False)
    hero.moveXY(x, y)
    hero.toggleFlowers(True)
    steps = size * 2
    direction = Math.sign(loopNum)
    stepAngle = twoPi / steps / direction
    loops = direction * loopNum
    stepSize = size / steps / loops
    curSize = 0
    angle = startAngle
    endAngle = (twoPi * loopNum) + startAngle
    while ternary((angle>=endAngle),(loopNum<0),(angle<=endAngle)):
        newX = x + curSize * Math.cos(angle)
        newY = y + curSize * Math.sin(angle)
        hero.moveXY(newX, newY)
        angle += stepAngle
        curSize += stepSize
    newX = x + size * Math.cos(endAngle)
    newY = y + size * Math.sin(endAngle)
    hero.moveXY(newX, newY)
 
redX = {"x": 28, "y": 36}
whiteX = {"x": 60, "y": 36}

# --------------------------------------------------
whiteX2 = {'x': 60, 'y': 42}
#setFlowerColor
hero.setFlowerColor("red")
# Draw a "3D style" box, using the drawPolygon and drawSpokes functions, centered on the red X and with a size of 10.
# The simplest startAngles to calculate would be either "up" or "down".
# The drawing functions deal with angles in terms of radians. If you think in terms of degrees then please use the "degreesToRadians(degrees)" function so they can understand you.
#drawPolygon(center, size, number of sides, start angle)
drawPolygon(redX, 10, 6, degreesToRadians(90))
#drawSpokes(center, size, number of spokes, start angle)
drawSpokes(redX, 10, 3, degreesToRadians(30))
# Draw the star bib, using the drawStar and drawSpiral functions. (See the Guide for an image of the shapes.)
# The star is centered on the white X and has a size of 6.
# The spirals have a size of 15. To get a spiral to go the other direction give it a negative number of loops.
#setFlowerColor
hero.setFlowerColor("blue")
#drawStar(center, size, sides, skips, startAngle)
drawStar(whiteX, 6, 7, 3, degreesToRadians(90))
#setFlowerColor
hero.setFlowerColor("yellow")
#drawSpiral(center, size,  number of loops, start angle)
drawSpiral(whiteX2, 15, 1, 3 * Math.PI / 2)
#drawSpiral(center, size,  number of loops, start angle)
drawSpiral(whiteX2, 15, -1, 3 * Math.PI / 2)