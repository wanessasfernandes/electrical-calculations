import time

def cabeçalho(txt):
    print(linha())
    print(f'\U000026A1{txt}\U0001F9BF'.center(41))
    print(linha())

def linha():
    return '━' * 43

def leiaInt(msg):
    while True:
        try:
            n = input(msg).strip()
            return int(n)
        except:
            print('\033[1;31mERRO! Por favor, digite um número válido.\033[m')    

def menu(lista):
    cabeçalho(' O que você deseja calcular?')
    c = 1
    for item in lista:
        print(f'\033[1m[ {c} ]\033[m {item}', flush=True)
        time.sleep(0.5)
        c += 1
    print(linha())
    opc = leiaInt('\U0001F4BB  Escolha uma opção e pressione ENTER: ')
    return opc
    

