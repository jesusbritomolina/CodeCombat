# https://codecombat.com/play/level/buddys-name-a?
# The peasant wants to know your pet's name.

# Use this function as the handler for "hear" events.
def sayName(event):
    # The pet will say these in order when this function is called.
    pet.say("My name is Furious Beast.")
    pet.say("But my friends call me Fluffy.")
    
# Use pet.on("eventName", functionName) to add an event listener to your pet.
# In this case use "hear" and sayName with pet.on()!
pet.on("hear", sayName)

# You don't need to say anything this time!
# The peasant will do the talking.