# Hack case..
# ?b??
# ab

s = input()
t = input()
ng = 'UNRESTORABLE'
ls = len(s)
lt = len(t)
for i in range(ls - lt, -1, -1):
    ss = s[i : i+lt]
    for a, b in zip(ss, t):
        if a not in ('?', b):
            break
    else:
        ans = []
        for j in range(i):
            ans.append('a' if s[j] == '?' else s[j])
            
        ans.extend(list(t))
        
        for j in range(i + lt, ls):
            ans.append('a' if s[j] == '?' else s[j])
        print("".join(ans))
        exit()
print(ng)