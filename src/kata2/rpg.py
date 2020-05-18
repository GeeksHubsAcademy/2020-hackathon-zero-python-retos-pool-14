#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    string.ascii_letters += 'ñÑ'
    password_generator = ''
    while len(password_generator) < passLen:
        marcador = random.randint(0,9)
        letrasmarcador = random.randint(0, 9)
        singmarcador = random.randint(0, 9)
        numeromarcador = random.randint(0, 9)

        if marcador == letrasmarcador:
            password_generator += string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)]
            if len(password_generator) == passLen: break

        if marcador == numeromarcador:
            password_generator += string.digits[random.randint(0, len(string.digits)-1)]
            if len(password_generator) == passLen: break

        if marcador == singmarcador:
            password_generator += string.punctuation[random.randint(0, len(string.punctuation)-1)]
            if len(password_generator) == passLen: break

    return password_generator
