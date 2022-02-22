# https://codecombat.com/play/level/anonymous-bank?
# Encuentras las contraseñas y obten los tesoros.

# We intercepted a scout with an encoded message.
encodedMessage = hero.findNearest(hero.findFriends()).message
# Aquí almacenaremos contraseñas.
passwordArray = []
# All passwords have 5 letters.Todas las contraseñas verdaderas tienen 5 letras.
passwordLength = 5

# Split encodedMessage by using a ";" and save the words in a variable.
words = encodedMessage.split(";")
# Itera sobre todas las palabras.
for word in words:
    # Recorta cada palabra para remover los espacios blancos.
    wordt = word.trim()
    # Si la longitud de la palabra limpia es 5:
    if len(wordt)==5:
        # Append the cleaned word to passwordArray:
        passwordArray.push(wordt)


# Muevete hasta cada marca y di la contraseña correcta:
marksPos = [{"x": 12, "y": 14}, {"x": 38, "y": 38},
            {"x": 42, "y": 16}, {"x": 54, "y": 12}];
for i in range(4):
    pos = marksPos[i]
    hero.moveXY(pos.x, pos.y)
    password = passwordArray[i]
    if password:
        hero.say(password)
    else:
        hero.say("qwerty")