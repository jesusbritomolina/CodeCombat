# https://codecombat.com/play/level/zero-sum?
# Vence al héroe enemigo en dos minutos.
while True:
    enemies = hero.findEnemies()
    nearestEnemy = hero.findNearest(enemies)
    
    # Tu héroe puede recolectar monedas e invocar tropas.
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")
    
    # Ella también comanda tus aliados en batalla.
    friends = hero.findFriends()
    for friend in friends:
        hero.command(friend, "attack", friend.findNearest(enemies))
    
    # Usa las habilidades de tu héroe para cambiar el rumbo.
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)