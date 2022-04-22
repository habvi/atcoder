from itertools import product

A = list(map(int, list(input())))

for pm in product((1, -1), repeat=3):
    ans = [str(A[0])]
    total = A[0]
    for i in range(3):
        total += pm[i] * A[i + 1]
        ans.append('+' if pm[i] == 1 else '-')
        ans.append(str(A[i + 1]))

    if total == 7:
        print("".join(ans) + "=7")
        exit()



# a, b, c, d = map(int, input())

# pm = (1, -1)
# ans = str(a)
# for i in pm:
#     for j in pm:
#         for k in pm:
#             if a + b * i + c * j + d * k == 7:
#                 ans += ('+' if i == 1 else '-') + str(b)
#                 ans += ('+' if j == 1 else '-') + str(c)
#                 ans += ('+' if k == 1 else '-') + str(d)
#                 print(ans + '=7')
#                 exit()