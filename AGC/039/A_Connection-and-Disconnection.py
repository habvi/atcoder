from itertools import groupby

S = input()
n = len(S)
K = int(input())

if len(set(S)) == 1:
    print(n * K // 2)
    exit()

ans = 0
A = []
for k, v in groupby(S):
    num = len(list(v))
    A.append(num)
    ans += num // 2

ans *= K

if S[0] == S[-1]:
    left = A[0]
    right = A[-1]
    ans -= (left//2 + right//2) * (K - 1)
    ans += ((left + right)//2) * (K - 1)

print(ans)