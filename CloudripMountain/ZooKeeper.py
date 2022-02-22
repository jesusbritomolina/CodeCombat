# https://codecombat.com/play/level/zoo-keeper?
# Protege la jaula
# Pon un soldado en cada X
points = [{"x": 33, "y": 42},
          {"x": 47, "y": 42},
          {"x": 33, "y": 26},
          {"x": 47, "y": 26}]

# Reúne 80 de oro.
while hero.gold < 80:
    item = hero.findNearestItem()
    hero.move(item.pos)
# Crea 4 soldados.
for i in range(4):
    hero.summon("soldier")
    
# Envía a tus soldados en posición.
while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy and enemy.team == "ogres" and friend.distanceTo(enemy) < 5:
            hero.command(friend, "attack", enemy)
            pass
            
        else:
            hero.command(friend, "move", point)
            pass