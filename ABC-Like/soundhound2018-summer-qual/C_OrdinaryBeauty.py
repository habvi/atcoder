# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_c

n, m, d = map(int, input().split())

if d == 0:
    p = n
else:
    p = (n - d) * 2

num = m - 1
total = n * n
print(p / total * num)