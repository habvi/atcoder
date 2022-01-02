S = input()
t = []
for s in S:
    if s == '6':
        t.append('9')
    elif s == '9':
        t.append('6')
    else:
        t.append(s)
print("".join(t)[::-1])