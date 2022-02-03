from itertools import permutations

n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

d = list(permutations(range(1, n + 1)))

print(abs(d.index(P) - d.index(Q)))