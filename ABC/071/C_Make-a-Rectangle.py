from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)

two = [0, 0]
four = [0]
for k, v in c.items():
    if v >= 4:
        four.append(k)
    elif v >= 2:
        two.append(k)
two.sort()
four.sort()
print(max(four[-1] ** 2, two[-1] * two[-2], four[-1] * two[-1]))