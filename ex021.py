nome = str(input('Digite seu nome:')).strip()
print('Analisando seu nome...')
print('Seu nome todo maiusculo é...{}'.format(nome.upper()))
print('Seu nome minusculo é...{}'.format(nome.lower()))
print('seu nome tem {} letras sem contar os espaços'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))

filme = str(input('Digite um filme:')).strip()
troca = str(input('Digite uma palavra aleatória:')).strip()
s1 = filme.split()
print(filme.replace(s1[1],troca))
