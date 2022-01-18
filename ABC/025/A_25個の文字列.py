from itertools import product
s = input()
n = int(input())
pr = sorted(product(s, repeat=2))
print("".join(pr[n - 1]))



# s = input()
# n = int(input())
# a = []
# for i in s:
#     for j in s:
#         a.append(i + j)
# print(a[n - 1])