n, q = map(int, input().split())
abv = [-1]*n
und = [-1]*n
table = [i+1 for i in range(n)]

for _ in range(q):
    f, t, x = map(int, input().split())
    f, t, x = f-1, t-1, x-1
    a = table[f] # to table[t]
    b = table[t] # to und[x]
    c = und[x] # to table[f]
    table[t] = a
    und[x] = b
    table[f] = c

ans = [-1]*n
for i, t in enumerate(table):
    if t == -1:
        continue
    else:
        ans[t-1] = i+1

    while True:
        if und[t-1] == -1:
            break
        ans[und[t-1]-1] = i+1
        t = und[t-1]
print(*ans, sep='\n')