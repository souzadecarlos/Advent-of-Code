
# Duas funções:
# - Conta pontos da jogada:
# 1: Rock, 2: Paper, 3: Scissors
# - Conta pontos do resultado:
#   - Vitória: A/Y, B/Z, C/X - 6 pts
#   - Empate: A/X, B/Y, C/Z - 3 pts
#   - Derrota: A/Z, B/X, C/Y - 0 pts

def pontos_jogada(jogada):
    if jogada[1] == "X":
        return(1)
    elif jogada[1] == "Y":
        return(2)
    else:
        return(3)

def resultado_jogada(jogada):
    if ((jogada[0] == "A" and jogada[1] == "Y") or (jogada[0] == "B" and jogada[1] == "Z") or
       (jogada[0] == "C" and jogada[1] == "X")): return(6)
    elif ((jogada[0] == "A" and jogada[1] == "X") or (jogada[0] == "B" and jogada[1] == "Y") or
       (jogada[0] == "C" and jogada[1] == "Z")): return(3)
    else:
        return(0)

file = "Day 2\input.txt"

with open(file) as f:

    soma = 0

    for line in f:
        jogada = line.split()
        pontuacao = (pontos_jogada(jogada) + resultado_jogada(jogada))
        soma += pontuacao
        print(f"{jogada}: {pontuacao} - {soma}")

