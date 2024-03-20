S = list(input())

pop_a = 0
while S and S[-1] == 'a':
    S.pop()
    pop_a += 1

i = 0
while i != len(S) and S[i] == 'a' and pop_a != i:
    i += 1
S = S[i:]

print("Yes" if S == S[::-1] else "No")
