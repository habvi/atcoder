S = input()

if S[0] == '1':
    print("No")
    exit()

num = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]
pin = 0
for i, x in enumerate(num):
    for y in x:
        if S[y] == '1':
            pin |= 1 << i

for i in range(7):
    for j in range(i + 2, 7):
        if (pin >> i & 1) and (pin >> j & 1):
            for k in range(i + 1, j):
                if not pin >> k & 1:
                    print("Yes")
                    exit()
print("No")