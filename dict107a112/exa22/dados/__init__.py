def valid(n):
    n = str(input(n)).replace(',', '.')
    while True:
        if n.isalpha() or n.strip() == '':
            print(f'\033[0;31mERRO!"{n}" é um valor invalido! \033[m')
            n = str(input('Digite novamente o valor do produto: ')).replace(',', '.')
        else:
            break
    return float(n)
