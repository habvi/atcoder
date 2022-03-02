n = int(input())
H = list(map(int, input().split()))

H[0] -= 1
for i in range(1, n):
    if H[i] > H[i - 1]:
        H[i] -= 1
    elif H[i] == H[i - 1]:
        continue
    else:
        print('No')
        exit()

print('Yes')