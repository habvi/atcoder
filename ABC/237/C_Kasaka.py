S = list(input())

if S == S[::-1]:
    print('Yes')
    exit()

front = 0
for s in S:
    if s == 'a':
        front += 1
    else:
        break

tail = 0
while S and S[-1] == 'a':
    S.pop()
    tail += 1

if front > tail:
    print('No')
    exit()

S = S[front:]

print('Yes' if S == S[::-1] else 'No')