from collections import defaultdict

n = int(input())
num = defaultdict(int)
for _ in range(n):
    a = int(input())
    if a in num:
        del num[a]
    else:
        num[a] += 1

print(len(num))



# from collections import Counter

# n = int(input())
# A = [int(input()) for _ in range(n)]

# ans = 0
# for _, v in Counter(A).items():
#     if v % 2:
#         ans += 1
# print(ans)