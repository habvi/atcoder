def ceil(a, b):
    return (a + b - 1) // b


n = int(input())

print(ceil(n, 1000) * 1000 - n)