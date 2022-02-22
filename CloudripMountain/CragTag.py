# https://codecombat.com/play/level/crag-tag?
# Alcanza a  Pender Spellbane para aprender sus secretos.

while True:
    # Pender is the only friend here, so she's always the nearest.
    pender = hero.findNearest(hero.findFriends())

    if pender:
        # moveXY() moverá a donde Pender esta,
        # pero ella se habrá alejado para el momento en que llegas allí.
        #hero.moveXY(pender.pos.x, pender.pos.y)
        
        # move() solo mueve un paso a la vez,
        # así que puedes usarlo para rastrear a tu blanco.
        hero.move(pender.pos)