from lib.interface import *  # Importa funções de interface
from time import sleep  # Importa a função sleep para pausas na exibição


def exibir_calculo(formula, valores, resultado, unidade):
    """
    Exibe a fórmula utilizada, os valores aplicados e o resultado final do cálculo.
    Adiciona pequenas pausas para melhorar a experiência do usuário.
    """
    print('\U0001F9E9 Fórmula:', formula)
    sleep(1)
    print(f'\U0001F4D0 Cálculo: {valores}')
    sleep(1)
    print(f'\U00002705 Resultado: {resultado:.1f} {unidade}')
    return resultado


def leiOhm(v=0, i=0, r=0, esc=0):
    """
    Aplica a Lei de Ohm para calcular resistência, tensão ou corrente.
    A escolha do cálculo é feita através do parâmetro 'esc'.
    """
    print('\U0001F4D6 Aplicando a Lei de Ohm:\n')
    sleep(1)

    try:
        if esc == 1:
            if i == 0: # garante que não tera divisão por zero
                raise ZeroDivisionError("Corrente não pode ser zero.")
            return exibir_calculo('R = V ÷ I', f'R = {v} V ÷ {i} A', v / i, 'Ω')

        elif esc == 2:
            return exibir_calculo('V = I × R', f'V = {i} A × {r} Ω', i * r, 'V')

        elif esc == 3:
            if r == 0: # garante que não tera divisão por zero
                raise ZeroDivisionError("Resistência não pode ser zero.")
            return exibir_calculo('I = V ÷ R', f'I = {v} V ÷ {r} Ω', v / r, 'A')

        else:
            print('\033[1;31mERRO! Opção inválida.\033[m')

    except Exception as e:
        print(f'\033[1;31mErro inesperado: {e}\033[m\n')



def leiJoule(p=0, i=0):
    """
    Aplica a Lei de Joule para calcular resistência com base na potência e corrente.
    """
    print('\U0001F4D6 Aplicando a Lei de Joule:\n')
    sleep(1)

    try:
        if i == 0:
            raise ZeroDivisionError("Corrente não pode ser zero.")
        return exibir_calculo('R = P ÷ I²', f'R = {p} W ÷ {i**2:.1f} A²', p / i**2, 'Ω')
    
    except Exception as e:
        print(f'\033[1;31mErro inesperado: {e}\033[m\n')


def potência(p=0, i=0, v=0, r=0, esc=0):
    """
    Calcula a potência elétrica com base nas variáveis disponíveis.
    A opção escolhida é definida pelo parâmetro 'esc'.
    """
    print('\U0001F4D6 Aplicando a relação de potência:\n')
    sleep(1)

    try:
        if esc == 1:
            if i == 0:
                raise ZeroDivisionError("Corrente não pode ser zero.")
            return exibir_calculo('V = P ÷ I', f'V = {p} W ÷ {i} A', p / i, 'V')

        elif esc == 2:
            if v == 0:
                raise ZeroDivisionError("Tensão não pode ser zero.")
            return exibir_calculo('I = P ÷ V', f'I = {p} W ÷ {v} V', p / v, 'A')

        elif esc == 3:
            return exibir_calculo('P = V × I', f'P = {v} V × {i} A', v * i, 'W')

        elif esc == 4:
            return exibir_calculo('P = R × I²', f'P = {r} Ω × {i**2:.2f} A²', r * i**2, 'W')

        else:
            print('\033[1;31mERRO! Opção inválida.\033[m')

    except Exception as e:
        print(f'\033[1;31mErro inesperado: {e}\033[m\n')
