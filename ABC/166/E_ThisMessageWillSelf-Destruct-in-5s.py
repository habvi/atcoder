from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

X, Y = [], []
for i, a in enumerate(A):
    X.append(i + a)
    Y.append(i - a)

num = defaultdict(int)
ans = 0
for x, y in zip(X, Y):
    ans += num[y]
    num[x] += 1
print(ans)


# |j - i| = Ai + Aj
# i < j
# j - i = Ai + Aj
# i + Ai = j - Aj