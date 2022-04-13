n, K = map(int, input().split())

zero = n // K
ans = pow(zero, 3)

if K % 2 == 0:
    half = zero + ((n % K) >= K // 2)
    ans += pow(half, 3)
print(ans)



# from collections import defaultdict

# n, K = map(int, input().split())

# mod = defaultdict(int)
# for i in range(1, n + 1):
#     mod[i % K] += 1

# ans = pow(mod[0], 3)
# if K % 2 == 0:
#     ans += pow(mod[K // 2], 3)
# print(ans)