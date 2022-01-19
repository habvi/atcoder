n = int(input())
n2 = 2 * n
s = list(input())
q = int(input())

def mask(x):
    if flg:
        return (x + n) % n2
    else:
        return x

flg = 0
for _ in range(q):
    t, a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if t == 1:
        s[mask(a)], s[mask(b)] = s[mask(b)], s[mask(a)]
    else:
        flg = 1 - flg

print("".join(s[n:] + s[:n]) if flg else "".join(s))