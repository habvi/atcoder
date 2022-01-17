from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
for v in Counter(a).values():
    if v >= 2:
        ans += v - 1
print(ans)



# from collections import Counter
# n = int(input())
# a = [int(input()) for _ in range(n)]
# print(n - len(Counter(a)))