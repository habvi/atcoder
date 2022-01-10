L = int(input())
L -= 1
nmrt = 1
dnmnt = 1
for i in range(1, 12):
    nmrt *= L
    L -= 1
    dnmnt *= i
print(nmrt // dnmnt)