v1 = float(input('Digite o valor a ser pago R$: '))
cond = int(input('Digite:\n'
                 '1 Para pagamento á vista em dinheiro\n'
                 '2 Para pagamento á vista no cartão\n'
                 '3 Para pagamento em até 2x no cartão\n'
                 '4 Para pagamento em 3x ou mais no cartão\n'
                 'Digite a opção desejada: '))
if cond == 1:
    valor = v1 * 0.9
elif cond == 2:
    valor = v1 * 0.95
elif cond == 3:
    valor = v1
elif cond == 4:
    valor = v1 * 1.2
else:
    print('Opção invalida! Tente novamente!'),
print(f'Com essa opção de pagamento escolhida o valor a ser pago será R$:{valor}')
