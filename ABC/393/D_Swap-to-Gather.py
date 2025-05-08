def calc(S):
    to_right = []
    one, total = 0, 0
    for i, s in enumerate(S):
        if s == '1':
            one += 1
        else:
            total += one
        to_right.append(total)
    return to_right


N = int(input())
S = input()

to_left = calc(S[::-1])[::-1]
to_right = calc(S)

ans = float('inf')
for i in range(N):
    ans = min(ans, to_left[i] + to_right[i])
print(ans)
