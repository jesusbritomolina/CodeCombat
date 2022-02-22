# https://codecombat.com/play/level/double-queue?
# Use potions to heal soldiers and swords to arm peasants.

# Watch for the item and unit queues.
while True:
    item = hero.findNearestItem()
    unit = hero.findNearestFriend()
    if not item or not unit:
        continue
    # Use "type" property to distinguish units and items
    # if the item is "potion" and the unit is "soldier":
    if item.type == 'potion' and unit.type == "soldier":
        # Say the unit name (id):
        hero.say(unit.id)
    # if the item is "sword" and the unit is "peasant":
    elif item.type == 'sword' and unit.type == "peasant":
        # Say the unit name (id):
        hero.say(unit.id)
    # Otherwise say "Next" (or anything else).
    hero.say("Next")