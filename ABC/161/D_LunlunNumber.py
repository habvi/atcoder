k = int(input())
if k <= 10:
    print(k)
    exit()

a = 10
for _ in range(k - 10):
    sa = str(a)
    if set(sa) == {'9'}:
        a += 1
        continue
        
    for i in range(len(sa) - 2, -1, -1):
        if int(sa[i]) + 1 == int(sa[i + 1]) or sa[i] == sa[i + 1] == '9':
            continue
        else:
            inc = i
            break
    else:
        t = [str(int(sa[0]) + 1)]
        for i in range(len(sa) - 1):
            t.append(str(max(0, int(t[-1]) - 1)))
        a = int("".join(t))
        continue

    t = []
    for i in range(len(sa)):
        if i == inc:
            t.append(sa[i])
            t.append(str(int(sa[i + 1]) + 1))
            break
        t.append(sa[i])

    for i in range(len(sa) - len(t)):
        t.append(str(max(0, int(t[-1]) - 1)))
    a = int("".join(t))
print(a)