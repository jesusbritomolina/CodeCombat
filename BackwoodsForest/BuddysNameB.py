# https://codecombat.com/play/level/buddys-name-b?
# La mascota debe saludar al héroe y al campesino.

#  Usa esta función como un controlador para eventos "hear"(oír):
def sayHello(event):
    # La mascota dice hola:
    pet.say("Saludos.")

#  Usa el procedimiento .on("eventType", functionName)[.cuandoPasa("TipoDeEvento",NombreDeFunción)] de la mascota.
# En este nivel la mascota debe usar sayHello cuando "hear"(oye) algo.
pet.on("hear", sayHello)

# Entonces saluda a la mascota y espera una respuesta.
hero.say("¡Hola, mi amigo!")