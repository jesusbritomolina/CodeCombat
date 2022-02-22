# https://codecombat.com/play/level/sarven-savior?
# Una LISTA (array) es una lista de ítems.

# Esta lista es una lista de los nombres de tus amigos.
friendNames = ['Joan', 'Ronan', 'Nikita', 'Augustus']

# Los índices en la lista empiezan en 0, no en 1!
friendIndex = 0

# Buclea cada nombre en la lista.
# La función len() te da la longitud de la lista.
while friendIndex < len(friendNames):
    # Usa corchetes para conseguir un nombre de la lista.
    friendName = friendNames[friendIndex]
    
    # Dile a tu amigo que se vaya a casa.
    # Usa + para concatenar dos strings.
    hero.say(friendName + ', go home!')
    
    # Incrementa friendIndex para conseguir el siguiente nombre de la lista.
    friendIndex += 1
    
# Vuelve y construye una "fence" para mantener a los ogros afuera.
hero.moveXY(18, 30)
hero.buildXY("fence", 30, 30)