n = int(input())
d = list(map(int, input().split()))
d.sort()
h = n // 2
print(d[h] - d[h - 1])