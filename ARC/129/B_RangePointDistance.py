n = int(input())
r_min = float('inf')
l_max = 0
for i in range(n):
    l, r = map(int, input().split())
    r_min = min(r_min, r)
    l_max = max(l_max, l)
    
    if r_min >= l_max:
        print(0)
    else:
        print((l_max - r_min + 1) // 2)