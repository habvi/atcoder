n = int(input())
A = list(map(int, input().split()))

k = 30

one = [0] * k
zero = [0] * k
for a in A:
    for i in range(k):
        if a >> i & 1:
            one[i] += 1
        else:
            zero[i] += 1

ans = sum(A)
for a in A:
    exp = 1
    bit_sum = 0
    for i in range(k):
        if a >> i & 1:
            bit_sum += zero[i] * exp
        else:
            bit_sum += one[i] * exp
        exp *= 2

    ans = max(ans, bit_sum)

print(ans)