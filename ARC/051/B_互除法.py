k = int(input())

a = 1
b = 1
for _ in range(k):
    a, b = a + b, a

print(a, b)