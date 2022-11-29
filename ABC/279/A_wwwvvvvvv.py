from collections import Counter

S = input()

c = Counter(S)
print(c['v'] + c['w'] * 2)