n = int(input())
D, X = map(int, input().split())

num = [0] * (D + 1)
for _ in range(n):
    a = int(input())
    for i in range(1, D + 1, a):
        num[i] += 1

print(sum(num) + X)



# def ceil(a, b):
#     return (a + b - 1) // b


# n = int(input())
# D, X = map(int, input().split())

# ans = 0
# for _ in range(n):
#     a = int(input())
#     ans += ceil(D, a)
# print(ans + X)