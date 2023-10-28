from itertools import count

N = int(input())

for i in count(N):
    s = str(i)
    if int(s[0]) * int(s[1]) == int(s[2]):
        print(i)
        exit()