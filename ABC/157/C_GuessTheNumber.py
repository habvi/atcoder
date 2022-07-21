n, m = map(int, input().split())

num = [set() for _ in range(n)]
for _ in range(m):
    s, c = map(int, input().split())
    if n != 1 and s == 1 and c == 0:
        print(-1)
        exit()
    s -= 1
    num[s].add(c)

ans = []
for i, st in enumerate(num):
    if len(st) >= 2:
        print(-1)
        exit()
    ans.append(str(st.pop()) if st else '0')

if n != 1 and ans[0] == '0':
    ans[0] = '1'
print(''.join(ans))