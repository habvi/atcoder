n, r = map(int, input().split())
S = input()

if S.count('o') == n:
    print(0)
    exit()

ls = list(S)
tail = S.rfind('.')

ans = 0
for i, s in enumerate(ls):
    if i + r - 1 >= tail:
        ans += 1 if i == 0 else 2
        break
    
    if s == '.':
        ans += 1
        for j in range(r):
            ls[i + j] = 'o'
    if i != 0:
        ans += 1
    
print(ans)