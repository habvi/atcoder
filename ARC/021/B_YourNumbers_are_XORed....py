L = int(input())
B = [int(input()) for _ in range(L)]

ans = []
now = 0
for b in B:
    ans.append(now)
    now ^= b

if ans[0] ^ ans[-1] == B[-1]:
    for a in ans:
        print(a)
else:
    print(-1)