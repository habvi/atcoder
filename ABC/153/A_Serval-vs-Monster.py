def ceil(a, b):
    return (a + b - 1) // b

H, A = map(int, input().split())
print(ceil(H, A))
