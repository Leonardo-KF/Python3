c = ''
maior = soma = cont = 0
menor = 99999
while c != 'N':
    n1 = int(input('Digite um numero: '))
    soma += n1
    cont += 1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    c = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
m = soma / cont
print(f'Você Digitou {cont} números e a média deles foi: {m}\n'
      f'O maior valor digitado foi {maior}\n'
      f'O menor valor digitado foi {menor}')
