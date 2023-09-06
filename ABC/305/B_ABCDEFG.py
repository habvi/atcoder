p, q = input().split()

ALPH = "A..BC...DE....F........G"
print(abs(ALPH.index(p) - ALPH.index(q)))