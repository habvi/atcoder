from itertools import count

n = int(input())

ac = [1]
for i in count(2):
    ac.append(ac[-1] + i)
    if ac[-1] >= n:
        break

m = len(ac) - 1

diff = ac[m] - n
for i in range(1, m + 2):
    if diff and i == diff:
        continue
    print(i)