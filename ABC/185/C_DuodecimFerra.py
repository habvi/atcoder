L = int(input())
L -= 1
nmrt = 1
dnmnt = 1
for i in range(1, 12):
    nmrt *= L
    L -= 1
    dnmnt *= i
print(nmrt // dnmnt)



# from math import factorial
# def P(n, r):
#     return factorial(n) // factorial(n - r)

# def C(n,r):
#     return P(n, r) // factorial(r)

# L = int(input())
# print(C(L - 1, 11))