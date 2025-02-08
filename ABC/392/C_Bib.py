N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans = []
for i, num in enumerate(Q):
    ans.append((num, Q[P[i] - 1]))
ans.sort()
for _, zekken in ans:
    print(zekken)
