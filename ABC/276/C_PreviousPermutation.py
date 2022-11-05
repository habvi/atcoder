N = int(input())
P = list(map(int, input().split()))

ans = P[:]
seen = [0] * N
for i, p in enumerate(P[::-1]):
    for j in reversed(range(p)):
        if seen[j]:
            ans[N - i - 1] = j + 1
            rep = P[N - i:]
            rep.remove(j + 1)
            rep.append(p)
            ans[N - i:] = sorted(rep, reverse=True)
            print(*ans)
            exit()
    seen[p - 1] = 1
