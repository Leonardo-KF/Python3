mi = mu = hom = 0
while True:
    print('=' * 19)
    print('CADASTRO DE PESSOAS')
    print('=' * 19)
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    print('-' * 23)
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        mi += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mu += 1
    if op == 'N':
        break
print(f'Foram cadastradas {mi} pessoas maiores de 18 anos!\n'
      f'Foram cadastrados {hom} homens no total\n'
      f'E {mu} mulheres com menos de 20 anos!')
print('=' * 16)
print('Fim do programa!')
