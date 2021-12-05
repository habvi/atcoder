n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
d = []
for i in range(m - 1):
    d.append(x[i + 1] - x[i])
d.sort(reverse= True)
print(sum(d) - sum(d[:n - 1]))