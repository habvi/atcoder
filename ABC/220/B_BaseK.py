def n_to_deci(X, base):
    num = 0
    for x in X:
        num = num * base + x
    return num


K = int(input())
A, B = input().split()
A = list(map(int, list(A)))
B = list(map(int, list(B)))

a = n_to_deci(A, K)
b = n_to_deci(B, K)
print(a * b)