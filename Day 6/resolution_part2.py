
with open("Day 6/input.txt") as f:
    signal = f.readlines()[0]

def find_marker(signal, size):

    for pos, i in enumerate(signal):
        marker = signal[pos:pos+size]
        if len(set(marker)) == size:
            posicao = pos + size
            break
    
    return(posicao)

print(find_marker(signal, 14))