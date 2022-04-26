n = int(input())
D, X = map(int, input().split())

ans = n + X
for _ in range(n):
    a = int(input())
    ans += (D - 1) // a
print(ans)



# n = int(input())
# D, X = map(int, input().split())

# num = [0] * (D + 1)
# for _ in range(n):
#     a = int(input())
#     for i in range(1, D + 1, a):
#         num[i] += 1

# print(sum(num) + X)