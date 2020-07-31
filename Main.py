import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import * #works for pyqt5
from PyQt5.QtWidgets import *
#import PyQt5

#import os
#import classes
from repos.classes import *
from repos.Methods import *
Armas = []
Consumiveis = []
Armaduras = []
Aneis = []

arquivo = open( os.getcwd() + "\\" + "test.txt", "r")

fileRead(Armas,Consumiveis,Armaduras,Aneis)

for item in Consumiveis:
    pass

# Função chamada quando botão “Hello” for acionado
# responsável pela alteração do “TextLabel”

# Criamos a aplicação principal
"""
app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.move(300, 300)
w.setWindowTitle('Simple')
w.show()




sys.exit(app.exec_())
"""