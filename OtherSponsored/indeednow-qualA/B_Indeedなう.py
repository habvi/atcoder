n = int(input())
s = sorted("indeednow")
for _ in range(n):
    t = sorted(input())
    if s == t:
        print('YES')
    else:
        print('NO')