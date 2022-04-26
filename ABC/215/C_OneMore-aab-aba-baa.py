from itertools import permutations

S, K = input().split()
K = int(K)

lis = set(permutations(S))
print(''.join(sorted(lis)[K - 1]))