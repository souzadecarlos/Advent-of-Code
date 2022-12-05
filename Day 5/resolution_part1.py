
with open("Day 5/input.txt") as f:
    
    pilhas = [[] for _ in range(9)]
    instrucoes = []

    for line in f:
        line = line.replace("\n", "")
        if line.startswith("["):
            line = line.replace("    ", ' [0]').split(" ")
            for pos, i in enumerate(line):
                pilhas[pos].append(i)
        elif line.startswith("m"):
            line = line.split(" ")
            instrucoes.append([int(line[1]), int(line[3]), int(line[5])])

for pos, x in enumerate(pilhas):
    pilhas[pos] = [y.replace("[","").replace("]","") for y in x if y != "[0]"]
    pilhas[pos] = "".join(pilhas[pos])

def mover(pilha, movimento):

    quantidade, posicao_inicial, posicao_final = movimento

    blocos = pilha[posicao_inicial-1][0:quantidade][::-1]
    pilha[posicao_final-1] = blocos + pilha[posicao_final-1]
    pilha[posicao_inicial-1] = pilha[posicao_inicial-1][quantidade:]

    return(pilha)

for i in instrucoes:
    pilhas = mover(pilhas, i)

print("".join([x[0] for x in pilhas]))
