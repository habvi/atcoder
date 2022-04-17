from collections import Counter

s1 = input()
s2 = input()
s3 = input()
n = len(s1) // 2

c1 = Counter(s1)
c2 = Counter(s2)
c3 = Counter(s3)

mn, mx = 0, 0
for al, num3 in c3.items():
    num1, num2 = c1[al], c2[al]
    if num1 + num2 < num3:
        print('NO')
        exit()

    mn += max(0, num3 - num2)
    mx += min(num1, num3)

print('YES' if mn <= n <= mx else 'NO')