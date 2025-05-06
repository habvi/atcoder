S = list(input())

ans = []
while S:
    if len(S) >= 2 and ''.join(S[-2:]) == "WA":
        S[-2:] = ['A', 'C']
    ans.append(S.pop())
print(''.join(ans[::-1]))
