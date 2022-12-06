
with open("Day 6/input.txt") as f:
    signal = f.readlines()[0]

for pos, i in enumerate(signal):
    marker = signal[pos:pos+4]
    if len(set(marker)) == 4:
        posicao = pos + 4
        print(posicao)
        break

