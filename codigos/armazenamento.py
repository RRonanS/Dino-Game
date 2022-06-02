def recorde():
    with open('dados.txt', 'r') as arq:
        l = arq.readlines()
    try:
        l1 = l[0].split(' ')
        val = int(l1[2])
    except:
        val = 0
    return val


def salvar(atual):
    anterior = recorde()
    if atual > anterior:
        with open('dados.txt', 'w') as arq:
            arq.write(f'recorde = {atual}')
