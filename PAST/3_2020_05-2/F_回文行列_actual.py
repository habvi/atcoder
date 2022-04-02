n = int(input())
al = 'abcdefghijklmnopqrstuvwxyz'
b = [[False]*26 for _ in range(n)]

for i in range(n):
    for a in input():
        b[i][al.index(a)] = True

ans = ''
if n%2 == 0:
    for i in range(n//2):
        for j, (s, t) in enumerate(zip(b[i], b[n-i-1])):
            if s and t:
                ans += al[j]
                break
        else:
            print(-1)
            exit()
    print(ans + ans[::-1])
else:
    for i in range(n//2):
        for j, (s, t) in enumerate(zip(b[i], b[n-i-1])):
            if s and t:
                ans += al[j]
                break
        else:
            print(-1)
            exit()

    for i, tf in enumerate(b[n//2]):
        if tf:
            print(ans + al[i] + ans[::-1])
            exit()