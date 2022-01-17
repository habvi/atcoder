n = int(input())
s = input()
t = 'b'
ans = 0
for i in range(n // 2):
    if i % 3 == 0:
        t = "".join(('a', t, 'c'))
    elif i % 3 == 1:
        t = "".join(('c', t, 'a'))
    else:
        t = "".join(('b', t, 'b'))
    ans += 1
print(ans if s == t else -1)