n = int(input())
ng = [int(input()) for _ in range(3)]
if n in ng:
    print('NO')
    exit()

for _ in range(100):
    for i in (3, 2, 1):
        if n - i not in ng:
            n -= i    
            break
    else:
        break
print('YES' if n <= 0 else 'NO')