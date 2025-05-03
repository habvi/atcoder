from itertools import product
from collections import defaultdict

N, M = map(int, input().split())
C = list(map(int, input().split()))
zoo = defaultdict(list)
for animal in range(M):
    _, *A = map(int, input().split())
    for a in A:
        zoo[a - 1].append(animal)

INF = float('inf')
ans = INF
for p in product((0, 1, 2), repeat=N):
    animals = defaultdict(int)
    price = 0
    for i, visit in enumerate(p):
        if visit == 1:
            for animal in zoo[i]:
                animals[animal] += 1
            price += C[i]
        elif visit == 2:
            for animal in zoo[i]:
                animals[animal] += 2
            price += C[i] * 2
    if len(animals) == M and all(animal >= 2 for animal in animals.values()):
        ans = min(ans, price)
print(ans)
