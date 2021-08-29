s = str(input('Digite seu sexo: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Opção invalida! Digite seu sexo novamente: ')).strip().upper()[0]
if s == 'M':
    s = 'Masculino'
if s == 'F':
    s = 'Feminino'
print(f'Sexo {s} registrado!')
