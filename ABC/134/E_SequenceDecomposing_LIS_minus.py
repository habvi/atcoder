from bisect import bisect

n = int(input())
A = [-int(input()) for _ in range(n)]

num = [-float('inf')]
ans = 0
for a in A:
    if num[-1] <= a:
        num.append(a)
        ans += 1
    else:
        num[bisect(num, a)] = a

print(ans)