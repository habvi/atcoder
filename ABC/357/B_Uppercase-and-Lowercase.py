S = input()

lower, upper = 0, 0
for s in S:
    if s.islower():
        lower += 1
    else:
        upper += 1

if lower < upper:
    print(S.upper())
else:
    print(S.lower())
