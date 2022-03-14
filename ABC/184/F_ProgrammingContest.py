from bisect import bisect

def times(A):
    res = []
    m = len(A)
    for bit in range(1 << m):
        time_ = 0
        for i in range(m):
            if bit >> i & 1:
                time_ += A[i]
        res.append(time_)
    return res


n, t = map(int, input().split())
A = list(map(int, input().split()))

mid = n // 2
left = times(A[:mid])
right = times(A[mid:])
right.sort()

ans = 0
for num in left:
    if num >= t:
        continue
    bi = bisect(right, t - num)
    ans = max(ans, num + right[bi - 1])

print(ans)