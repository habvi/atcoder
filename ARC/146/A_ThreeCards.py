from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

B = sorted(A)[-3:]
ans = 0
for per in permutations(B):
    S = ''.join(map(str, per))
    ans = max(ans, int(S))
print(ans)