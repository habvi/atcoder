from collections import defaultdict
n = int(input())
mx = 100
xyh = [tuple(map(int, input().split())) for _ in range(n)]

d = defaultdict(int)
for x, y, h in xyh:
    d[h] += 1
if 0 in d and len(d) == 2:
    for x, y, h in xyh:
        if h:
            print(x, y, h)
            exit()

for i in range(mx + 1):
    for j in range(mx + 1):
        H = set()
        for x, y, h in xyh:    
            if h == 0:
                continue
            
            dst = abs(y - i) + abs(x - j)
            H.add(h + dst)
            
        if len(H) == 1:
            print(j, i, list(H)[0])
            exit()
