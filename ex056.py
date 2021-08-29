idades = 0
mid = 0
idade = 0
nome = ''
for g in range(1, 5):
    print('='*10, F'{g}° PESSOA', '='*10)
    n1 = str(input('Digite o nome: ')).strip().upper()
    n2 = int(input('Digite a idade: '))
    n3 = str(input('Digite o sexo M/F: ')).strip()
    idades += n2
    if n3 in 'FffemininoFEMININO' and n2 < 20:
        mid += 1
    if n3 in 'MmasculinoMASCULINO' and g == 1:
        nome = n1
        idade += n2
    if n3 in 'mMmasculinoMASCULINO' and idade < n2:
        idade = n2
        nome = n1
    if nome == '':
        nome = 'Não há homens'
print(f'A média de idades das pessoas é de {idades/4}\n'
      f'O Homem mais velho é: {nome} e sua idade é {idade}\n'
      f'E existem {mid} mulher com menos de 20 anos')
