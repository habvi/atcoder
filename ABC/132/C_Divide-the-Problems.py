n = int(input())
d = list(map(int, input().split()))

d.sort()
i = n // 2
print(d[i] - d[i - 1])