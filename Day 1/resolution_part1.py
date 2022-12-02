# Resposta: Nº de calorias que cada elfo está carregando
# Cada espaço significa a mudança de elfo

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

lista_duendes = "".join(lines).replace("\n", " ").split("  ")

maior_caloria = 0

for duende in lista_duendes:
    try:
        duende = list(map(int, duende.split(" ")))
        soma = sum(duende)
        if soma > maior_caloria:
            maior_caloria = soma
    except:
        pass

print(maior_caloria)