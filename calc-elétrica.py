from lib.interface import *
from lib.arquivo import *

while True:

    resp = menu(['\U0001F4CF  Resistência (R)', '\U0001F50B  Tensão      (V)', '\U0001F50C  Corrente    (I)', '\U0001F4A5  Potência    (P)', '\U0001F6E0   Dimensionamento', '\U0000274C  Sair do programa'])
    if resp == 1:
        escResis()
    if resp == 2:
        escTen()

    if resp == 3:
        print()

    if resp == 4:
        print()

    if resp == 5:
        print()

    if resp == 6:
        break
        



'''u = i*r
p = i*u

-> calculo de resistencias 
'''

