N = int(input())

if N == 0:
    print(0)
    exit()

ans = []
while N != 0:
    if N % 2:
        ans.append('1')
        N -= 1
    else:
        ans.append('0')
    N //= -2
print(''.join(ans[::-1]))