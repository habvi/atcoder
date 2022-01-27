from bisect import bisect

def get_each_sum(A):
    sm = []
    n = len(A)
    for bit in range(1 << n):
        tot = 0
        for i in range(n):
            if bit >> i & 1:
                tot += A[i]
        sm.append(tot)
    return sm
        

n, t = map(int, input().split())
A = list(map(int, input().split()))
mid = n // 2

a1 = get_each_sum(A[:mid])
a2 = get_each_sum(A[mid:])
a2.sort()

ans = 0
for a in a1:
    bi = bisect(a2, t - a)
    if not bi:
        continue
    ans = max(ans, a + a2[bi - 1])
print(ans)