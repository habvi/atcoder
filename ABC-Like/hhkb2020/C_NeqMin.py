n = int(input())
p = list(map(int, input().split()))
s = set()
mn = 0
for i in range(n):
    s.add(p[i])
    while mn in s:
        mn += 1
    print(mn)