def x_to_n_base(x, n):
    if (int(x / n)):
        return x_to_n_base(int(x / n), n) + str(x % n)
    return str(x % n)

n, k = map(int, input().split())
a = x_to_n_base(n, k)
print(len(str(a)))