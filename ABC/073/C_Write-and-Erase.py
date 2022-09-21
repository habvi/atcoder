N = int(input())

s = set()
for _ in range(N):
    a = int(input())
    if a in s:
        s.remove(a)
    else:
        s.add(a)
print(len(s))


# --------------------------------
# from collections import Counter

# n = int(input())
# A = [int(input()) for _ in range(n)]

# ans = 0
# for v in Counter(A).values():
#     ans += (v % 2)
# print(ans)