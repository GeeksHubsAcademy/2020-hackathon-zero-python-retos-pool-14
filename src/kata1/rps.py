from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
# 'Empate!'
# 'Ganaste!'
# 'Perdiste!'


def quienGana(player, ai):
    result = ''
    print(player.capitalize())
    print(ai.capitalize())
    player_input = player.capitalize()
    ai_input = ai.capitalize()

    position_player = options.index(player_input)
    position_ai = options.index(ai_input)
    print(position_player)
    print(position_ai)
    if position_player == position_ai:
        result = 'Empate!'

    if((position_player == 0 and position_ai == 1) or (position_player == 1 and position_ai == 2) or (position_player == 2 and position_ai == 0)):
        result = 'Perdiste!'
        
    if((position_player == 0 and position_ai == 2) or (position_player == 1 and position_ai == 0) or (position_player == 2 and position_ai == 1)):
        result = 'Ganaste!'

    return result

# Entry Point


def Game():
    #
    #

    #
    #

    winner = quienGana(player, ai)

    print(winner)
