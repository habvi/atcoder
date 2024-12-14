from itertools import accumulate

N, S = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
S %= total

ac = [0] + list(accumulate(A))
rac = set(accumulate(A[::-1]))
rac.add(0)

for x in ac:
    if (S - x) % total in rac:
        print("Yes")
        exit()

print("No")
