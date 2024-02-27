from collections import Counter

S = input()
c = Counter(S)
for (alph, num) in c.items():
    if num == 1:
        print(S.find(alph) + 1)
