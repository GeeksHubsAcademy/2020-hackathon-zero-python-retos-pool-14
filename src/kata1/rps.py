import random

options = ["Piedra", "Papel", "Tijeras"]
options = [option.lower() for option in options]
# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player= player.lower()
    ai = ai.lower()
    message = ''
    if player == ai:
        message = 'Empate!'
    else:
        if player == options[0]:
            if ai == options[1]:
                message = 'Perdiste!'
            else:
                message = 'Ganaste!'
        elif player == options[1]:
            if ai == options[0]:
                message = 'Ganaste!'
            else:
                message = 'Perdiste!'
        elif player == options[2]:
            if ai == options[0]:
                message = 'Perdiste!'
            else:
                message = 'Ganaste!'
    return message


# Entry Point
def Game():
    #
    #
    
    #
    #
    player = input("Escriba una opción:: Piedra, Papel o Tijeras::").lower()
    ai = random.choice(options)
    print("AI :: "+ai)
    winner = quienGana(player, ai)

    print(winner)
