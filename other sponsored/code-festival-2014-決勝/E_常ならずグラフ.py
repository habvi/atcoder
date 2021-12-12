n = int(input())
a = list(map(int, input().split()))
if n < 3:
    print(0)
    exit()

if a[0] < a[1]:
    a = [float('inf')] + a
else:
    a = [-float('inf')] + a

if a[-2] > a[-1]:
    a.append(float('inf'))
else:
    a.append(-float('inf'))
    
up = 1 if a[0] < a[1] else 0
i = 0
s = []
cnt = 0
while i <= n:
    if not up and a[i] < a[i + 1]:
        s.append(a[i])
        up = 1
        cnt += 1
    if up and a[i] > a[i + 1]:
        s.append(a[i])
        up = 0
        cnt += 1
    i += 1
print(0 if cnt <= 2 else len(s))