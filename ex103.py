jogador = {}
partidas = []
jogador['nome'] = str(input('Qual o nome do jogador?'))
p = int(input('Quantas partidas ele jogou?'))

for c in range(0,p):
    partidas.append(int(input(f'    Quantos gols na partida {c}:')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')
for i ,v in enumerate(jogador['gols']):
    print(f'    =>Na partida {i},fez {v} gols.')
print(f'    =>Foi um total de {jogador["total"]} de gols.')