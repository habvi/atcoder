def fin():
    print("No")
    exit()


S = input()

l = len(S)
if l != 8:
    fin()

if 'A' <= S[0] <= 'Z' and 'A' <= S[-1] <= 'Z':
    if S[1] == '0':
        fin()
    for i in range(1, 7):
        if not '0' <= S[i] <= '9':
            fin()
    print("Yes")
else:
    print("No")