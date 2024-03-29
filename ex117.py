def notas(*n,sit = False):
    """
    ->Função para analisar as notas e a situação de vários alunos
    :param n:uma ou mais notas dos alunos
    :param sit:valor opcional,indicando se deve ou não mostrar a situação
    :return:dicionário com várias informações
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >=5:
            r['situação'] = 'razoável'
        else:
            r['situação'] ='ruim'
    return r

resp = notas(5.5,9,10,6,sit = True)
print(resp)
help(notas)
