n, m = map(int, input().split())

a = (m + 1) // 2
b = m - a
for i in range(a):
    print(a - i, a + i + 1)
    
for i in range(b):
    s = a * 2 + b
    print(s - i, s + i + 2)