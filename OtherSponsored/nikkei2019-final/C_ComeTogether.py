def median_idx(A):
    num = 0
    for idx, a in enumerate(A):
        num += a
        if num > mid:
            return idx

def times(A, idx):
    sum_t = 0
    for i, a in enumerate(A):
        sum_t += a * abs(i - idx)
    return sum_t


h, w, K = map(int, input().split())
R = [w] * h
C = [h] * w

for _ in range(K):
    r, c = map(lambda x: int(x) - 1, input().split())
    R[r] -= 1
    C[c] -= 1

total = h * w - K
mid = total / 2

sum_r = times(R, median_idx(R))
sum_c = times(C, median_idx(C))
print(sum_r + sum_c)