n, m, t = map(int, input().split())
A = [0]
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a)
    A.append(b)
A.append(t)
       
d = n 
for i in range(m * 2 + 1):
    if i % 2:
        d = min(n, d + A[i + 1] - A[i])    
    else:
        d -= A[i + 1] - A[i]

    if d <= 0:
        print('No')
        exit()
print('Yes')