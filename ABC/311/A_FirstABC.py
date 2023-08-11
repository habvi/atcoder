N = int(input())
S = input()

abc = set()
for i, s in enumerate(S, 1):
    abc.add(s)
    if len(abc) == 3:
        print(i)
        exit()