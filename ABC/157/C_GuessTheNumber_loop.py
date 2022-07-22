N, M = map(int, input().split())
sc = [tuple(map(int, input().split())) for _ in range(M)]

for i in range(10 ** N):
    num = str(i)
    if len(num) != N:
        continue

    for s, c in sc:
        s -= 1
        if num[s] != str(c):
            break
    else:
        print(num)
        exit()
print(-1)