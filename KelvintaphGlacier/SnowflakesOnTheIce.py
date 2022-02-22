# https://codecombat.com/play/level/snowflakes-on-the-ice?
# For this level we need to a line fractal for the ground and a hexagonal snowflake made up of 6 line fractals. Check the guide for an image of the desired output.

def degreesToRadians(degrees):
    # All vector operations require working in radians rather than degrees.
    return Math.PI / 180 * degrees
    
# This function creates a line fractal.  Read through it so you understand the recursive concept.
def line(start, end):
    # First we need to get the full vector and its magnitude to determine if we are below our minimum threshold.
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    if distance < 4:
        # If under our threshold distance, then we will simply draw a line along the vector and be done (the return tells us to exit the function).
        hero.toggleFlowers(False)
        hero.moveXY(start.x, start.y)
        hero.toggleFlowers(True)
        hero.moveXY(end.x, end.y)
        return
        
    # Otherwise we will create our fractal by getting a vector of half magnitude.
    half = Vector.divide(full, 2)
    
    # We will be creating 4 line fractals (start -> A, A -> B, B -> A, and A -> end) and so we need to calculate the intermediate positions A and B.
    A = Vector.add(half, start)
    
    # To get B, we need to rotate the vector half 90 degrees and multiply by 2/3 (so it is 1/3 of the original magnitude), then add this to A.
    rotate = Vector.rotate(half, degreesToRadians(90))
    rotate = Vector.multiply(rotate, 2 / 3)
    B = Vector.add(rotate, A)

    # Now just draw the 4 lines using the line functions.
    line(start, A)
    line(A, B)
    line(B, A)
    line(A, end)


def flake(start, end):
    # To create a hexagonal flake we need to create 6 line fractals rotated by 60 degrees each time.
    side = Vector.subtract(end, start)
    a = start
    b = end
    for i in range(6):
        line(a, b)
        # To get the next edge, we need to rotate the side 60 degrees.
        a = b
        side = Vector.rotate(side, degreesToRadians(60))
        # Now need to reset a and b with the beginning and end points for the new side.
        b = Vector.add(side, a)

whiteXs = [Vector(12, 10), Vector(60, 10)]
redXs = [Vector(64, 52), Vector(52, 52)]

# You need to actually call the functions with a start and end vector for each.
line(whiteXs[0], whiteXs[1])
# Be sure to use actual Vector objects–simple objects will not work.
flake(redXs[0], redXs[1])
# Refresh often to avoid a memory leak and crash (working on it)