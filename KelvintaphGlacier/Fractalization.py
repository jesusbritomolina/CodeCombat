# https://codecombat.com/play/level/fractalization?
# Check the guide for the description of the problem
# Aquí están algunas funciones apra ayudarte a dibujar als curvas

def degreesToRadians(degrees):
    # All vector operations require working in radians rather than degrees.
    return Math.PI / 180 * degrees
    
def koch(start, end):
    # This function will draw a Koch Curve between two Vector positions
    # Start by creating a vector from start to end using Vector.subtract.
    # full = ...
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    
    # Use the magnitude of the vector to check for the stop condition.
    if distance < 3:
        # Move into position and draw the line, don't forget to toggle flowers properly.
        hero.toggleFlowers(False)
        hero.moveXY(start.x, start.y)
        hero.toggleFlowers(True)
        hero.moveXY(end.x, end.y)
        return
    
    # Need to draw 4 shorter Koch curves with sides 1/3 the length.
    # We will calculate the 3 intermediate points, A, B, & C.
    # We just need the point that is one-third of the full Vector from the start Vector.
    third = Vector.multiply(full, 1 / 3)
    A = Vector.add(start, third)
    # This one needs to be rotated 60 degrees from A but the same length.  Use rotate and add to get B.
    B = Vector.add(A, Vector.rotate(third, degreesToRadians(60)))
    # This point works out to adding another third to A.
    C = Vector.add(A, third)
    # Now we can draw the 4 curves connecting start, A, B, C, and end.
    koch(start, A);
    koch(A, B);
    koch(B, C);
    koch(C, end);
    
whiteXs = [Vector(6, 6), Vector(74, 6), Vector(74, 61), Vector(6, 61)]
hero.setFlowerColor("white");
koch(whiteXs[0], whiteXs[1]);
koch(whiteXs[1], whiteXs[2]);
koch(whiteXs[2], whiteXs[3]);
koch(whiteXs[3], whiteXs[0]);