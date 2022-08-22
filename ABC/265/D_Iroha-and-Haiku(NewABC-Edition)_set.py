from itertools import accumulate

N, P, Q, R = map(int, input().split())
A = [0] + list(map(int, input().split()))

ac = list(accumulate(A))
s = set(ac)
for x in ac:
    y = x + P
    z = y + Q
    w = z + R
    if (y in s) and (z in s) and (w in s):
        print("Yes")
        exit()
print("No")