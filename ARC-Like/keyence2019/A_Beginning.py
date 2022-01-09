a = list(map(int, input().split()))
a.sort()
if "".join(map(str, a)) == '1479':
    print('YES')
else:
    print('NO')