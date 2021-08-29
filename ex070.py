p1 = soma = pmb = conta = 0
mb = ' '
while True:
    pro = str(input('Digite o nome do produto: ')).strip().lower()
    pre = float(input('Digite o valor do produto: R$ '))
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    soma += pre
    conta += 1
    if pre > 1000:
        p1 += 1
    if conta == 1 or pre < pmb:
        mb = pro
        pmb = pre
    if cont == 'N':
        break
print(f'O valor total de sua compra é: R${soma:.2f}\n'
      f'Tem {p1} produtos que custam mais de R$1000.00\n'
      f'O produto mais barato é {mb} custando R${pmb:.2f}')
