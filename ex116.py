def leiaint(msg):
    ok = False
    valor =0
    while True:
        n = str(input((msg)))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[4;31mERRO!Digite um número válido.\033[m')
        if ok:
            break
    return valor
n = leiaint('Digite um número:')
print(f'O número digitado foi {n}.')