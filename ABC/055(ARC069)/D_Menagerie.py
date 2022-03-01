n = int(input())
S = input()
a = [[""] * n for _ in range(4)]
for i, (s, w) in enumerate(("SW", "WS", "SS", "WW")):
    a[i][0] = s 
    a[i][-1] = w

d = {"SWo" : "W", "SSx" : "W", "WWx" : "W", "WSo" : "W", "SWx" : "S", "SSo" : "S", "WSx" : "S", "WWo" : "S"}
for i in range(4):
    for j in range(n - 2):
        t = a[i][j] + a[i][j - 1] + S[j]
        a[i][j + 1] = d[t]

for i in range(4):
    ok = True
    t1 = a[i][-3] + a[i][-2] + S[-2]
    if d[t1] != a[i][-1]:
        ok = False
    t2 = a[i][-2] + a[i][-1] + S[-1]
    if d[t2] != a[i][0]:
        ok = False
    if ok:
        print("".join(a[i]))
        exit()
print(-1)