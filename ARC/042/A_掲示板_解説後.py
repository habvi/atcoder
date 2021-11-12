n, m = map(int, input().split())
s = [0]*n
ans = []
A = [int(input()) for _ in range(m)][::-1]
for i, a in enumerate(A):
    if s[a-1]: continue
    ans.append(a)
    s[a-1] = 1
    
ans += [i+1 for i, v in enumerate(s) if v == 0]
for a in ans:
    print(a)