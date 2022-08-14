A, B = input().split()

a = int(A)
b = int(B.replace('.', ''))

print(a * b // 100)