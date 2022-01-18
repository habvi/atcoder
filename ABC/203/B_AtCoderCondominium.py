n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    for j in range(1, k + 1):
        ans += i * 100 + j
print(ans)



# O(1)
# def f(x):
#     return x * (x + 1) // 2
# n, k = map(int, input().split())
# print(100 * f(n) * k + f(k) * n)