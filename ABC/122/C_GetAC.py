n, q = map(int,input().split())
s = input()
a = [0]*n
cnt = 0
A = 0
for i in range(n):
    if s[i] == 'A':
        A = 1
    elif A == 1 and s[i] == 'C':
        cnt += 1
        A = 0
    else:
        A = 0
    a[i] = cnt
    
for i in range(q):
    l, r = map(int,input().split())
    print(a[r-1]-a[l-1])