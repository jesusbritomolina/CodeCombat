# https://codecombat.com/play/level/olympic-race?
# The pet must win the race.
# Runners should touch their teams mark and run back.

def onHear(event):
    referee = pet.findNearestByType("wizard")
    # If the referee is speaker and the message is "Start":
    if referee == event.speaker and event.message == "Start":
        # Make the pet run to the red mark.
        pet.moveXY(54, 27)
        # Then run back.
        pet.moveXY(6, 27)

# Assign the onHear function to handle "hear" events.
pet.on("hear", onHear)