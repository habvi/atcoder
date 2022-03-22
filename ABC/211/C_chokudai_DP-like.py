from collections import defaultdict

S = input()
MOD = 10**9 + 7
WORD = 'Xchokudai'

count_ = defaultdict(int)
count_[0] = 1

for s in S:
    if s in WORD:
        i = WORD.index(s)
        count_[i] += count_[i - 1]
        count_[i] %= MOD

print(count_[len(WORD) - 1])