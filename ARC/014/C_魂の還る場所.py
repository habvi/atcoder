from collections import Counter

n = int(input())
S = input()

ans = 0
for _, v in Counter(S).items():
    ans += v % 2
print(ans)