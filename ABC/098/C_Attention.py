n = int(input())
s = input()
w, e = [0], [0]
for i in range(n):
    if s[i] == 'W':
        w.append(w[-1] + 1)
    else:
        w.append(w[-1])

for i in range(n - 1, -1, -1):
    if s[i] == 'E':
        e.append(e[-1] + 1)
    else:
        e.append(e[-1])
w = w[1:]
e = e[1:][::-1]

ans = float('inf')
for i in range(n):
    if i == 0:
        ans = min(ans, e[i + 1])
    elif i == n - 1:
        ans = min(ans, w[i])
    else:
        ans = min(ans, w[i] + e[i + 1])
print(ans)