
file = "Day 2\input.txt"

def pontos_total(jogada):

    vitoria = {"A": "B", "B": "C", "C": "A"}
    derrota = {"A": "C", "B": "A", "C": "B"}

    if jogada[1] == "Z":
        pts = pontos_jogada(vitoria[jogada[0]]) + 6
    elif jogada[1] == "Y":
        pts = pontos_jogada(jogada[0]) + 3
    else:
        pts = pontos_jogada(derrota[jogada[0]])

    return(pts)


def pontos_jogada(resposta):
    if resposta == "A":
        return(1)
    elif resposta == "B":
        return(2)
    else:
        return(3)

with open(file) as f:

    soma = 0

    for line in f:
        jogada = line.split()
        soma += pontos_total(jogada)

        