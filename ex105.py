def notas(*lst, sit=False):
    """
    => Função para analisar o desempenho de uma turma com base nas notas
    :param lst: Uma ou mais notas dos alunos
    :param sit: (opcional) Mostra a situação da turma
    :return: Dicionario com varios dados sobre a turma
    """
    n1 = {}
    # mai = men = med = 0
    # for i, c in enumerate(lst):
        # if i == 0:
           # mai = men = med = c
        #else:
            # med += c
            # if c > mai:
             #   mai = c
            # if c < men:
              #  men = c
    n1['total'] = len(lst)
    n1['maior'] = max(lst)
    n1['menor'] = min(lst)
    n1['media'] = sum(lst)/len(lst)
    if sit:
        if n1['media'] >= 7:
            n1['Situação'] = 'Boa'
        elif n1['media'] >= 5:
            n1['Situação'] = 'Razoavel'
        else:
            n1['Situação'] = 'Ruim'
    return n1


resp = notas(8.8, 10, 6.8, 6, 8, 1, sit=True)
print(resp)
