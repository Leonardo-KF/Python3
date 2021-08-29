def lint(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido!\033[m')
        if ok:
            break
    return valor

num = lint('digite um numero: ')
print(f'Voce digitou o numero {num}')