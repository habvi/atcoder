a, b, c = map(int, input().split())
bc = pow(b, c, 4)
bc = bc + 4 if bc == 0 else bc
print((a % 10)**bc % 10)



# a, b, c = map(int, input().split())
# ak = []
# k = a % 10
# for _ in range(4):
#     ak.append(k)
#     k *= a % 10
#     k %= 10
# bc = pow(b, c, 4)
# print(ak[bc - 1])