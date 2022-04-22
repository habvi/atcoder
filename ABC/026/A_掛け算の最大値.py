A = int(input())

ans = 0
for i in range(1, A):
    for j in range(1, A + 1):
        if i + j == A:
            ans = max(ans, i * j)
print(ans)



# A = int(input())
# x = A // 2
# print(x * x)