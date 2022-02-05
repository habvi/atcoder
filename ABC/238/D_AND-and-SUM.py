T = int(input())

for _ in range(T):
    a, s = map(int, input().split())
    if a * 2 > s:
        print('No')
        continue

    x = s - a * 2
    fin = False
    for i in range(60):
        if x >> i & 1 and a >> i & 1:
            print('No')
            fin = True
            break

    if not fin:
        print('Yes')