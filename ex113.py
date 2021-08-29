def lint(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Você não digitou um numero inteiro!\033[m')
            continue
        else:
            return n1


def lfloat(msg):
    while True:
        try:
            n1 = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO! Você não digitou um numero real! \033[m')
            continue
        else:
            return n1


num = lint('Digite um numero: ')
num1 = lfloat('Digite um numero real: ')
print(f'Voce digitou o numero {num} e o {num1}')