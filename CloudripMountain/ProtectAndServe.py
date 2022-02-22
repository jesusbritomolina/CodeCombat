# https://codecombat.com/play/level/protect-and-serve?
# Protect the workers and animals!

# Defend these two positions:
defend = []
defend[0] = { "x": 98, "y": 28 }
defend[1] = { "x": 84, "y": 7 }

soldiers = []

friends = hero.findFriends()
for index in range(len(friends)):
    friend = friends[index]
    if friend.type == "soldier":
        soldiers.append(friend)
    else:
        # Defend the workers:
        defend.append(friend)

while True:
    # Use a for-loop to assign each soldier to a corresponding defend[] target
    # Use command(soldier, "defend", thang) or command(soldier, "defend", position)
    i = 0
    for soldier in soldiers:
        hero.command(soldier, "defend", defend[i])
        i += 1
    pass