from collections import Counter

W = input()
ans = True
for k, v in Counter(W).items():
    if v % 2:
        ans = False
        break
print('Yes' if ans else 'No')