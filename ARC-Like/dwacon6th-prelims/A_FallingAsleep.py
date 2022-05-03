n = int(input())
st = [tuple(input().split()) for _ in range(n)]
X = input()

ans = 0
start = False
for s, t in st:
    if start:
        ans += int(t)
    if s == X:
        start = True
print(ans)