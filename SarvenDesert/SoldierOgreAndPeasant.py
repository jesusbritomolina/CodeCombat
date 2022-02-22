# https://codecombat.com/play/level/soldier-ogre-and-peasant?
# Traslada a la trinidad al lado izquierdo del rio.

# El soldado odia al ogro.
soldier = pet.findNearestByType("soldier")
# El ogro planea algo mal contra el campesino.
ogre = pet.findNearestByType("munchkin")
# Solo un campesino.
peasant = pet.findNearestByType("peasant")

# Usa pet.carryUnit(unit, x, y) para trasladar a las unidades.
left = {'x':32,'y':38}
right = {'x':53,'y':41}

pet.carryUnit(ogre, left.x, left.y)
pet.carryUnit(soldier, left.x, left.y)
pet.carryUnit(ogre, right.x, right.y)
pet.carryUnit(peasant, left.x, left.y)
pet.carryUnit(ogre, left.x, left.y)