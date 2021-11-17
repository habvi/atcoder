n = int(input())
S = input()
k1 = [0]*10
k2 = set()
k3 = set()
for s in S:
    add_k2 = set()
    for i, k in enumerate(k1):
        if k:
            add_k2.add(str(i) + s)

    k1[int(s)] = 1
    for k in k2:
        k3.add(k + s)
    k2 |= add_k2

print(len(k3))