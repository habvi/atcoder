n = int(input())
if n <= 2:
    print(n)
    exit()

a = []
cnt = 0
for i in range(1, n):
    cnt += i
    a.append((cnt, i))
    if cnt >= n:
        break

x = list(range(1, a[-1][1] + 1))
for i in range(1, len(x) + 1):
    if i == a[-1][0] - n:
        continue
    print(i)