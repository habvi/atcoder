s = int(input())
a = [s]
pre = s
i = 0
while True:
    if pre % 2 == 0:
        pre = a[-1] // 2
    else:
        pre = 3 * a[-1] + 1
    if pre in a:
        break
    a.append(pre)
    i += 1
print(i + 2)