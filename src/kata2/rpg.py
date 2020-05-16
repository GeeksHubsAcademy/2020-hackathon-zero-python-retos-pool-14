#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    
    #
    #
    result = ''
    for i in range(passLen):
        result += random.choice(string.printable)
    
    return result
