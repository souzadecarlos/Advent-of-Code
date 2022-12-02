with open("input.txt") as f:
    lines = f.readlines()

lista_duendes = "".join(lines).replace("\n", " ").split("  ")

def somar_duende(duende):
    try:
        duende = list(map(int, duende.split(" ")))
        soma = sum(duende)
        return(soma)
    except:
        return(0)

lista_soma = [somar_duende(x) for x in lista_duendes]

def pegar_top(lista, top_n):

    lista_sorted = sorted(lista, reverse = True)
    return(sum(lista_sorted[0:top_n]))

print(pegar_top(lista_soma, 3))
