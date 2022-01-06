n = int(input())
ans = 0
for i in range(1, n + 1):
    if i % 3 and i % 5:
        ans += i
print(ans)



# O(1)
# def Sn(n):
#     return n*(n + 1) // 2
# def S_adn(a, d, n):
#     return (2*a + (n - 1)*d) * n // 2

# n = int(input())
# print(Sn(n) - S_adn(3, 3, n // 3) - S_adn(5, 5, n // 5) + S_adn(15, 15, n // 15))