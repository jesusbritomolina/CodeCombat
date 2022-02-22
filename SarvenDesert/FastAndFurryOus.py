# https://codecombat.com/play/level/fast-and-furry-ous?
# Usa un manejador de eventos así la mascota y el héroe correrán juntos!

def petMove():
    pet.moveXY(50, 21)

# Usa pet.on("spawn", petMove) en vez de petMove().
# De esta manera, tu héroe y la mascota se moverán al mismo tiempo
pet.on("spawn", petMove) # Reemplaza esto con pet.on("spawn", petMove)

hero.moveXY(50, 12)