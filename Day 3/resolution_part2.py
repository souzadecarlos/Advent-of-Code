import string

def pontuacao(letras):

    total = 0

    letras = list(letras)
    minusculas = list(string.ascii_lowercase)
    maiusculas = list(string.ascii_uppercase)

    for letra in letras:
       
        if letra in maiusculas:
            total += maiusculas.index(letra) + 27
        elif letra in minusculas:
            total += minusculas.index(letra) + 1

    return(total)

def interseccao(grupo):

    iguais = set(grupo[0]).intersection(grupo[1]).intersection(grupo[2])
    pts = pontuacao(iguais)

    return(pts)

with open("Day 3/input.txt") as f:

    grupos = []
    contador = 0

    for line in f:

        if len(grupos) > contador:
            pass
        else:
            grupos.append([])

        line = line.replace("\n", "")

        grupos[contador].append(line)

        if len(grupos[contador]) > 2:
            contador += 1


soma = 0

for grupo in grupos:

    soma += interseccao(grupo)

print(soma)
