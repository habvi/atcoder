n = int(input())

pre = [1]
for i in range(2, n + 1):
    new = pre[:]
    new.append(i)
    new.extend(pre[:])
    pre = new

print(*pre)