def fat(n=1, show=False):
    """
    fat serve para calculo de fatorial
    :param n: O numero que terá o fatorial calculado
    :param show: (opcional) Mostrar ou não o calculo
    :return: O valor do fatorial do param n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
    return print(f'{f}')


# programa principal
fat(5, show=True)
