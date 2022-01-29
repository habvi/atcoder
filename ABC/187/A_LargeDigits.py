def f(x):
    return int(x[0]) + int(x[1]) + int(x[2])


a, b = input().split()
print(max(f(a), f(b)))