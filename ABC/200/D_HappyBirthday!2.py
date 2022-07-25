def calc(bit):
    total = 0
    lis = []
    for i in range(N):
        if bit >> i & 1:
            total += A[i]
            lis.append(i + 1)
    return total % MOD, lis


N = int(input())
A = list(map(int, input().split()))

MOD = 200
# 2**8 - 1 = 255 > 200
N = min(N, 8)
for bit1 in range(1, 1 << N):
    for bit2 in range(1, 1 << N):
        if bit1 == bit2:
            continue

        sum_b, B = calc(bit1)
        sum_c, C = calc(bit2)
        if sum_b == sum_c:
            print("Yes")
            print(len(B), *B)
            print(len(C), *C)
            exit()
print("No")