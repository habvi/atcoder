h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
s = [[""] * w for _ in range(h)]
now = 0
num = 1
for i in range(h):
    for j in range(w):
        if i % 2 == 1:
            s[i][w - j - 1] = num
        else:
            s[i][j] = num

        A[now] -= 1
        if not A[now]:
            now += 1
            num += 1
for t in s:
    print(*t)