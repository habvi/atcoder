n = int(input())
A = list(map(int, input().split()))

A.sort()
mn = A.pop(0)
mx = A.pop()

ans = []
for a in A:
    if a >= 0:
        ans.append((mn, a))
        mn -= a
    else:
        ans.append((mx, a))
        mx -= a

total = mx - mn
ans.append((mx, mn))

print(total)
for a, b in ans:
    print(a, b)