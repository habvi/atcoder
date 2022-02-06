n = int(input())

aoki = 0
A = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append((a, b, 2*a + b))
    aoki += a

A.sort(key=lambda x: -x[2])

ans = 0
takahashi = 0
for a, b, _ in A:
    aoki -= a
    takahashi += a + b
    ans += 1
    if aoki < takahashi:
        print(ans)
        exit()