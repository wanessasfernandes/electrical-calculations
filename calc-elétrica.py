# Importação de módulos personalizados e bibliotecas necessárias
from lib.interface import *
from lib.arquivo import *
import time

while True:
    '''
    Loop principal do programa que exibe o menu e processa as escolhas do usuário
    Exibe o menu de opções para o usuário e armazena a escolha na variável `resp`
    '''
    resp = menu([
        '\U0001F4CF  Resistência (R)',   
        '\U0001F50B  Tensão      (V)',  
        '\U0001F50C  Corrente    (I)',   
        '\U0001F4A5  Potência    (P)',   
        '\U0000274C  Sair do programa'  
    ])

    # Verifica qual opção o usuário escolheu e chama a função correspondente
    if resp == 1:
        calcular_resistência() 
    elif resp == 2:
        calcular_tensão()  
    elif resp == 3:
        calcular_corrente() 
    elif resp == 4:
        calcular_potência() 
    elif resp == 5:
        print("\nSaindo do programa... Até logo!")  
        time.sleep(0.5) 
        break  
    else:
        print('\n' + '\033[1;31mERRO! Por favor, digite um número válido.\033[m' + '\n') 
