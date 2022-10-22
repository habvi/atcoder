N, x, y = map(int, input().split())
A = list(map(int, input().split()))

dp_c = set()
dp_c.add(A[0])
for a in A[2::2]:
    ndp = set()
    for d in dp_c:
        ndp.add(d + a)
        ndp.add(d - a)
    dp_c = ndp

dp_r = set()
dp_r.add(0)
for a in A[1::2]:
    ndp = set()
    for d in dp_r:
        ndp.add(d + a)
        ndp.add(d - a)
    dp_r = ndp

if x in dp_c and y in dp_r:
    print("Yes")
else:
    print("No")