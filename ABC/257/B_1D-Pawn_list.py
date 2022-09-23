N, _, _ = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
L = list(map(int, input().split()))

km = [0] * N
for a in A:
    km[a] = 1

for l in L:
    ct = 0
    for i in range(N - 1):
        ct += (km[i])
        if ct == l:
            if km[i + 1]:
                break
            km[i + 1] = 1
            km[i] = 0
            break

for i in range(N):
    if km[i]:
        print(i + 1)