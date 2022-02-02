from collections import Counter

S = input()

if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

c = Counter(S)

for k in range(112, 1000, 8):
    mlt = Counter(str(k))
    if not mlt - c:
        print('Yes')
        exit()
print('No')