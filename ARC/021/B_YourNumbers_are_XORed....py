l = int(input())
b = [int(input()) for _ in range(l)]
a = [0, b[0]]

for i in range(1, l):
    a.append(a[-1] ^ b[i])

if a[0] == a[-1]:
    for ans in a[:-1]:
        print(ans)
else:
    print(-1)