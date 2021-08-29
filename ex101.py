def voto(n):
    from datetime import date
    n = date.today().year - n
    if n > 18:
        return 'Obrigatória'
    elif n >= 16 or n >= 65:
        return 'Opcional'
    else:
        return 'Negada'


u = int(input('Digite o ano do seu nascimento: '))
print(f'Você tem a condição de voto como: {voto(u)}')
