l, r = map(int, input().split())
MOD = 2019
a = [0]*MOD

for i in range(l, min(r, l + MOD)):
    for j in range(i+1, min(r+1, l + MOD)):
        a[i*j % MOD] = 1

print(a.index(1))