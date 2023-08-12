N = int(input())

C = []
dice = []
for _ in range(N):
    C.append(int(input()))
    A = list(map(int, input().split()))
    dice.append(A)
X = int(input())

cand = []
for i, d in enumerate(dice, 1):
    if X in d:
        cand.append((C[i - 1], i))
cand.sort()

if not cand:
    print(0)
    exit()
mn = cand[0][0]
ans = [i for c, i in cand if c == mn]
print(len(ans))
print(*ans)