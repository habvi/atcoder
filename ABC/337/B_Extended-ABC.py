S = input()

idx = []
for alph in "ABC":
    i = S.find(alph)
    if i != -1:
        idx.append(i)
    i = S.rfind(alph)
    if i != -1:
        idx.append(i)

print("Yes" if idx == sorted(idx) else "No")