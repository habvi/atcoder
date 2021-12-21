# python TLE, PyPy3 1336ms

n = int(input())
A = list(map(int, input().split()))
k = len(bin(max(A))) - 2
s = set()
for i, a in enumerate(A):
    s.add((a, i))

for i in range(k - 1, -1, -1):
    nxt = set()
    for a, j in s:
        if a&(1 << i):
            nxt.add((a, j))

    if len(nxt) >= 2:
        s = nxt

s = list(s)
a, b = s[0][0], s[1][0]
print(a + b - ((a&b) ^ (a|b)))