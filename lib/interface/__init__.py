import time

#Exibe um cabeçalho formatado
def cabeçalho(txt):
    print(linha())
    print(f'\U000026A1 {txt} \U0001F50C'.center(43))
    print(linha())

#Exibe um título formatado
def mostrar_titulo(titulo):
    print(linha())
    print(f'\n{titulo.center(43)}\n')
    print(linha())    

#Exibe a solicitação para escolha de fórmula
def mostrar_form():
    print('\n\U0001F4CC Qual fórmula você deseja utilizar?\n')

#Retorna uma linha separadora
def linha(): 
    return '━' * 43
   
#Adiciona um espaçamento visual com linha
def espaçamento():
    print('\n' + linha() + '\n')  

#Lê um número inteiro do usuário, garantindo entrada válida
def leiaInt(msg):
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print('\n' + '\033[1;31mERRO! Por favor, digite um número válido.\033[m' + '\n')    

#Lê um número float do usuário, garantindo entrada válida
def leiaFloat(msg):
    while True:
        try:
            return float(input(msg).strip().replace(',', '.'))
        except ValueError:
            print('\n' + '\033[1;31mERRO! Por favor, digite um número válido.\033[m' + '\n')     

#Exibe um menu de opções numeradas e retorna a escolha do usuário
def menu(lista):
    cabeçalho('O que você deseja calcular?')
    
    for i, item in enumerate(lista, start=1):
        print(f'\033[1m[ {i} ]\033[m {item}', flush=True)
        time.sleep(0.5)  # Pequena pausa para melhor exibição
    
    print(linha() + '\n')
    r = leiaInt('\U0001F4BB Escolha uma opção e pressione ENTER: ')
    print()
    return r

#Exibe uma lista de opções e retorna a escolha do usuário
def escolha(lista):
    for i, item in enumerate(lista, start=1):
        print(f'\033[1m[ {i} ]\033[m {item}', flush=True)
        time.sleep(0.5)
    
    espaçamento()
    r = leiaInt('\U0001F4BB Escolha uma opção e pressione ENTER: ')
    print()
    return r
