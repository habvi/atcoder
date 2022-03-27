from itertools import product

n = int(input())
for pr in product('abc', repeat=n):
    print("".join(pr))