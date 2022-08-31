S = input()

for i, s in enumerate(S):
    if i == 3:
        if s != '-':
            print("No")
            exit()
    else:
        if not s.isdigit():
            print("No")
            exit()
print("Yes")