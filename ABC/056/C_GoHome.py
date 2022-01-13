# O(1)
x = int(input())
a = int((x * 2) ** 0.5)
if a * (a + 1) >= x * 2:
    print(a)
else:
    print(a + 1)



# O(√N)
# x = int(input())
# for i in range(1, int((x * 2)**0.5) + 5):
#     if i * (i + 1) >= 2 * x:
#         print(i)
#         exit()