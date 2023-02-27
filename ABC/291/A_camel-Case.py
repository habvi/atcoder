S = input()

for i, s in enumerate(S):
    if 'A' <= s <= 'Z':
        print(i + 1)
        exit()
