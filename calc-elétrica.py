from lib.interface import *

while True:

    resp = menu(['\U0001F4CF  Resistência (R)', '\U0001F50B  Tensão      (V)', '\U0001F50C  Corrente    (I)', '\U0001F4A5  Potência    (P)', '\U0001F6E0   Dimensionamento', '\U0000274C  Sair do programa'])
    if resp == 1:
        print()
    if resp == 2:
        print()

    if resp == 3:
        print()

    if resp == 4:
        print()

    if resp == 5:
        print()

    if resp == 6:
        break
        

    else:
        print()
        print('\033[1;31mERRO! Digite um opção válida.\033[m')   
        print() 
