# https://codecombat.com/play/level/ace-of-coders?
# Venza al héroe enemigo en menos de tres minutos.
    
def buildArmy():
    # Tu héroe puede invocar y ordenar a tropas aliadas.
    buildOrder = ["soldier","soldier","soldier","soldier","soldier","soldier","soldier","soldier","soldier","soldier", "archer","soldier", "archer", "soldier", "archer"]  # "archer", "artillery", "arrow-tower"
    type = buildOrder[len(hero.built) % len(buildOrder)]
    if hero.gold >= hero.costOf(type):
        hero.summon(type)
    
def commandArmy():
    friends = hero.built
    enemies = hero.findEnemies()
    points = hero.getControlPoints()
    for i, friend in enumerate(friends):
        if friend.health <= 0 or friend.type == "arrow-tower":
            continue
        # Manda a tu ejército a capturar puntos de control.
        # Asegúrate de elegir tus puntos de control sabiamente.
        point = points[i % len(points)]
        if self.now() < 30:
            self.command(friend, "defend", point.pos)
        else:
            enemies = self.findEnemies()
            nearestEnemy = self.findNearest(enemies)
            self.command(friend, "attack", nearestEnemy)
    
def controlHero():
    enemies = hero.findEnemies()
    nearestEnemy = hero.findNearest(enemies)
    shouldAttack = hero.time > 90
    # Usa las habilidades de tu héroe para cambiar el rumbo.
    # if shouldAttack: ...
   
while True:
    buildArmy()
    commandArmy()
    controlHero()