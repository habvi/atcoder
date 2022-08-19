S = list(input())
n = len(S)

head = 0
while head < n and S[head] == 'a':
    head += 1

tail = 0
while S and S[-1] == 'a':
    S.pop()
    tail += 1

if not S:
    print("Yes")
    exit()

if head > tail:
    print("No")
    exit()

S = S[head:]
print("Yes" if S == S[::-1] else "No")