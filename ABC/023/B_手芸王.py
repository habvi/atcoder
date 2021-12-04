n = int(input())
s = input()
t = 'b'
a = [t]
for i in range(102):
    if i % 3 == 0:
        t = "".join(('a', t, 'c'))
    elif i % 3 == 1:
        t = "".join(('c', t, 'a'))
    else:
        t = "".join(('b', t, 'b'))
    a.append(t)
print(a.index(s) if s in a else -1)