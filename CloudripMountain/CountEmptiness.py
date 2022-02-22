# https://codecombat.com/play/level/count-emptiness?
# Solve the riddler puzzle and find the treasure.
# Count the whitespace on both sides of a riddle.

# This function moves the hero N steps right.
def moveNSteps(n):
    hero.moveXY(hero.pos.x + 8 * n, hero.pos.y)

# Read the riddle.
riddle = hero.findNearestEnemy().riddle
# Trim whitespace from both sides and store in a variable
trimmed = riddle.trim()
# Find the difference between the `riddle` and `trimmed` lengths:
spot = len(riddle)-len(trimmed)
# Use the result and moveNSteps function to move to the spot:
moveNSteps(spot)
# Say something there!
hero.say("hi")