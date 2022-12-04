

def contem_tudo(valores):
    
    trabalhos = valores.split(",")
    trabalhos = [list(map(int, x.split("-"))) for x in trabalhos]

    if ((trabalhos[1][0] >= trabalhos[0][0] and trabalhos [1][1] <= trabalhos[0][1]) or
        (trabalhos[0][0] >= trabalhos[1][0] and trabalhos [0][1] <= trabalhos[1][1])):
       return(1)
    else:
        return(0) 

def contem_parte(valores):
    trabalhos = valores.split(",")
    trabalhos = [list(map(int, x.split("-"))) for x in trabalhos]

    if ((trabalhos[1][0] >= trabalhos[0][0] and trabalhos [1][0] <= trabalhos[0][1]) or
        (trabalhos[0][0] >= trabalhos[1][0] and trabalhos [0][0] <= trabalhos[1][1])):
       return(1)
    else:
        return(0) 

with open("Day 4/input.txt") as f:

    soma_completo = 0
    soma_parte = 0

    for line in f:

        soma_completo += contem_tudo(line)
        soma_parte += contem_parte(line)


print(f"Parte 1: {soma_completo}\nParte 2: {soma_parte}")
