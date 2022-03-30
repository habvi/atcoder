from collections import defaultdict

n = int(input())
word = defaultdict(int)
for _ in range(n):
    S = ''.join(sorted(input()))
    word[S] += 1

ans = 0
for i in word.values():
    ans += i * (i - 1) // 2

print(ans)