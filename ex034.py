s1 = int(input('Digite seu salário R$: '))
if s1 >= 1250:
    print(f'Você ganhará 10% de aumento! Seu novo salario é: {s1*1.10:.2f}R$')
else:
    print(f'Você ganhará 15% de aumento! Seu novo salario é: {s1*1.15:.2f}R$')
