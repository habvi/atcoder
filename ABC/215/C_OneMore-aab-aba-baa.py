from itertools import permutations

S, K = input().split()
K = int(K)

ans = sorted(set(permutations(S)))[K - 1]
print(''.join(ans))