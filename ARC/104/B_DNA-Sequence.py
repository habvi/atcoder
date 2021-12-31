from collections import Counter
n, S = input().split()
n = int(n)
ans = 0
for i in range(n):
    a, t, c, g = 0, 0, 0, 0
    for j in range(i, n):
        if S[j] == 'A':
            a += 1
        elif S[j] == 'T':
            t += 1
        elif S[j] == 'C':
            c += 1
        else:
            g += 1
        if a == t and c == g:
            ans += 1
print(ans)
        
            

