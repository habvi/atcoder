def comb(n, r):
    n1, r = n + 1, min(r, n - r)
    nmrt = dnmnt = 1
    for i in range(1, r + 1):
        nmrt = nmrt * (n1 - i)
        dnmnt = dnmnt * i
    return nmrt // dnmnt


L = int(input())

L -= 12
print(comb(L + 11, 11))



# L = int(input())
# print(comb(L - 1, 11))