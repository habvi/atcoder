a, b, x = map(int, input().split())
if a > x:
    print('NO')
    exit()
print('YES' if x - a <= b else 'NO')



# print('YES' if a <= x <= a + b else 'NO')