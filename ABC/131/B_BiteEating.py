n, l = map(int, input().split())
a = [l + i - 1 for i in range(1, n + 1)]
a.sort(key=lambda x: abs(x))
print(sum(a) - a[0])