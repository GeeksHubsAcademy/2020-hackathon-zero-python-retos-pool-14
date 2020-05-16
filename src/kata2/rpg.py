#!/usr/bin/python

import random 
import string

def RandomPasswordGenerator(passLen=10):
    #
    #Genero una cadena con la suma de todos los posible valores, mayusculas, minusculas, numeros y caracteres
    valores = string.ascii_letters + string.digits + string.punctuation
    #print(valores)
    respuesta = ""
    respuesta = respuesta.join([random.choice(valores) for i in range(passLen)])
    print(respuesta)

    #
    #
    return respuesta

#RandomPasswordGenerator(100)