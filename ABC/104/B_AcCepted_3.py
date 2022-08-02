S = input()

upper_idx = []
upper = []
for i, s in enumerate(S):
    if s.isupper():
        upper_idx.append(i)
        upper.append(s)

if ''.join(upper) != "AC" or upper_idx[0] != 0 or not (2 <= upper_idx[1] <= len(S) - 2):
    print("WA")
else:
    print("AC")
