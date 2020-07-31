from repos.classes import *
import os
def fileRead(Armas, Consumiveis, Armaduras, Aneis):
    arquivo = open( os.getcwd() + "\\" + "test.txt", "r")
    for line in arquivo:
        buffer = line.split(";")
        if(buffer[4].find("\n") != -1):
            buffer[4] = buffer[4][:-1]

        item = Item(buffer[0],buffer[1],buffer[2],buffer[3])
        if(buffer[3] == 'consumable'):
            #item = Item(buffer[0],buffer[1],buffer[2],buffer[3])
            Consumiveis.append(item)
        elif(buffer[3] == 'weapon'):
            Armas.append(item)
    
        print (buffer)

def MoneyEncrypt(string, value):
    if(string == 'pp'):
        value *= 1000
    elif(string == 'gp'):
        value *= 100
    elif(string == 'sp'):
        value *= 10
    else:
        value = value
    return value