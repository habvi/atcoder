from collections import defaultdict

def total_except_self(s):
    global is_same_alph
    total = 0
    for k, v in num.items():
        if k != s:
            total += v
        else:
            is_same_alph = True
    return total


S = input()

num = defaultdict(int)
is_same_alph = False
ans = 0
for s in S:
    ans += total_except_self(s)
    num[s] += 1
ans += is_same_alph
print(ans)
