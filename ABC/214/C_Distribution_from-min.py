n = int(input())

S = list(map(int, input().split()))
T = list(map(int, input().split()))

mn = T.index(min(T))
ans = [T[mn]]
for i in range(mn, mn + n - 1):
    ans.append(min(ans[-1] + S[i % n], T[(i + 1) % n]))

ans = ans[n - mn:] + ans[:n - mn]
print(*ans)