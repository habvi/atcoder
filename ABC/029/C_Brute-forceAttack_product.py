from itertools import product
for pr in product('abc', repeat=int(input())):
    print("".join(pr))