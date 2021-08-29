def met(n=0, f=False):
    """
    => Função que calcula a metade de um valor
    :param f: Se o valor será formatado
    :param n: Valor a ser calculado
    :return: resultado do calculo
    """
    if f:
        return val(n / 2)
    return n / 2


def dob(n=0, f=False):
    """
    => valor a ser dobrado
    :param f: Se o valor será formatado
    :param n: valor a ser calculado
    :return: resultado do calculo
    """
    if f:
        return val(n * 2)
    return n * 2


def ju(n=0, j=0, f=False):
    """
    => Função que calcula o aumento de preço em % de um valor
    :param f: Se o valor será formatado
    :param n: valor a ser aumentado
    :param j: quantidade em % a ser aumentada
    :return: valor total com o aumento
    """
    j /= 100
    tot = (n * j) + n
    if f:
        return val(tot)
    return tot


def des(n=0, d=0, f=False):
    """
    => Função que calcula uma redução em % de um produto
    :param f: se o valor será formatado ou não
    :param n: O valor total
    :param d: o valor em % que será descontado
    :return: O valor total com a redução
    """
    d /= 100
    tot = n - (n * d)
    if f:
        return val(tot)
    return tot


def val(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resu(n, j, d):
    """
    => função para mostrar um resumo dos dados de um produto
    :param n: valor do produto
    :param j: valor a ser acrescentado no produto em %
    :param d: valor a ser descontado do produto em %
    :return: none
    """
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:"}\t{val(n):<10}')  # \t faz uma tabulação automatica
    print(f'{"Dobro do preço:"}\t\t{dob(n, True):<10}')
    print(f'{"Metade do preço:"}\t{met(n, True):<10}')
    print(f'{j:<3}% {"de aumento:"}\t{ju(n, j, True):<10}')
    print(f'{d:<3}% {"de redução:"}\t{des(n, d, True):<10}')
    print('='*30)


