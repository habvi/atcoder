n = int(input())
a = list(map(int, input().split()))
tot = 0
for i in range(n):
    tot = tot * 2 + a[i]
print(tot)