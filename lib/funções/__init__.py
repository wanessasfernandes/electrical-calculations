from lib.interface import *
from time import sleep

def leiOhm(v=0, i=0, r=0, esc=0):
    print('\U0001F4D6 Aplicando a Lei de Ohm: ')
    print()
    sleep(1)

    if esc == 1:
        print('\U0001F9E9 Fórmula: R = V / I')
        sleep(1)
        print(f'\U0001F4D0 Cálculo: R = {v} V / {i} A')
        sleep(1)
        resp = v/i
        print(f'\U00002705 Resultado: R = {(resp):.1f} Ω')
        return resp
    
    elif esc == 2:
        print('\U0001F9E9 Fórmula: V = I x R')
        sleep(1)
        print(f'\U0001F4D0 Cálculo: V = {i} A x {r} Ω')
        sleep(1)
        resp = i * r
        print(f'\U00002705 Resultado: V = {(resp):.1f} V')
        return resp
    
    elif esc == 3:
        print('\U0001F9E9 Fórmula: I = V / R')
        sleep(1)
        print(f'\U0001F4D0 Cálculo: I = {v} V / {r} Ω')
        sleep(1)
        resp = v / r
        print(f'\U00002705 Resultado: I = {(resp):.1f} A')
        return resp
    
    else:
        return 999
    
def leiJoule(p=0, i=0):
    print('\U0001F4D6 Aplicando a Lei de Joule: ')
    print()
    sleep(1)
    print('\U0001F9E9 Fórmula: R = P / I²')
    sleep(1)
    print(f'\U0001F4D0 Cálculo: R = {p} W / ({(i**2):.1f})² A')
    sleep(1)
    r = (p / i**2)
    print(f'\U00002705 Resultado: R = {r:.1f} Ω')
    return r

def pot(p, i, v, esc=0):
    print('\U0001F4D6 Aplicando a relação: ')
    print()
    sleep(1)

    if esc == 1:
        print('\U0001F9E9 Fórmula: V = P / I')
        sleep(1)
        print(f'\U0001F4D0 Cálculo: V = {p} W / {i} A')
        sleep(1)
        resp = p / i
        print(f'\U00002705 Resultado: V = {(resp):.1f} V')
        return resp
    
    elif esc == 2:
        print('\U0001F9E9 Fórmula: I = P / V')
        sleep(1)
        print(f'\U0001F4D0 Cálculo: I = {p} W / {v} V')
        sleep(1)
        resp = p / v
        print(f'\U00002705 Resultado: I = {(resp):.1f} A')
        return resp

def trab(t, q, esc=0):
    print('\U0001F4D6 Aplicando a relação: ')
    print()
    sleep(1)

    if esc == 1:
        print('\U0001F9E9 Fórmula: V = W / Q')
        sleep(1)
        print(f'\U0001F4D0 Cálculo: V = {t} J / {q} C')
        sleep(1)
        resp = t / q
        print(f'\U00002705 Resultado: V = {(resp):.1f} V')
        return resp    