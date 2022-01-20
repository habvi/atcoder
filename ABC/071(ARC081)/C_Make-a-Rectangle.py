from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)

two = [0, 0]
four = [0]
for k, v in c.items():
    if v >= 2:
        two.append(k)
    if v >= 4:
        four.append(k)

two.sort(reverse=True)
four.sort(reverse=True)
print(max(four[0] ** 2, two[0] * two[1]))