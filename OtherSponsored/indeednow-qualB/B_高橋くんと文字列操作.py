S = list(input())
T = list(input())

n = len(S)
for i in range(n):
    if S == T:
        print(i)
        exit()

    rm = S.pop()
    S = [rm, *S]

print(-1)