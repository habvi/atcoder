from itertools import combinations
a = list(map(int, input().split()))
sm = sum(a)
for i in range(1, 4):
    for com in combinations(a, i):
        tot = sum(com)
        if tot * 2 == sm:
            print('Yes')
            exit()
print('No')



# a = list(map(int, input().split()))
# a.sort()
# if a[0] + a[-1] == a[1] + a[2] or sum(a[:3]) == a[-1]:
#     print('Yes')
# else:
#     print('No')