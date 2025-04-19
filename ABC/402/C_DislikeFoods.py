from collections import defaultdict

N, M = map(int, input().split())

kinds = []
kokufuku = defaultdict(list)
for i in range(M):
    K, *A = map(int, input().split())
    kinds.append(K)
    for a in A:
        kokufuku[a].append(i)
B = list(map(int, input().split()))

ans = 0
for b in B:
    for i in kokufuku[b]:
        kinds[i] -= 1
        if not kinds[i]:
            ans += 1
    print(ans)
