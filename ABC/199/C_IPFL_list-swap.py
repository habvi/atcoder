n = int(input())
s = list(input())
q = int(input())
l = s[:n]
r = s[n:]

for _ in range(q):
    t, a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if t == 1:
        if b < n:
            l[a], l[b] = l[b], l[a]
        elif n <= a:
            r[a - n], r[b - n] = r[b - n], r[a - n]
        else:
            l[a], r[b - n] = r[b - n], l[a]
    else:
        l, r = r, l

print("".join(l + r))