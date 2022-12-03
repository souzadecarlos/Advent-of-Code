# Dividir cada compartimento em dois
# Verificar quais letras se repetem nos dois compartimentos

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

def interseccao(string):

    compartimento = string.replace("\n", "")
    pos_meio = int(len(compartimento)/2)
    primeiro_compartimento = compartimento[0:pos_meio]
    segundo_compartimento = compartimento[pos_meio:]
    iguais = set(primeiro_compartimento).intersection(segundo_compartimento)
    pts = pontuacao(iguais)

    return(pts)

with open("Day 3/input.txt") as f:

    soma = 0

    for linha in f:
        
        soma += interseccao(linha)

print(soma)