from collections import deque

S = deque(input())

rev = 0
for _ in range(int(input())):
    t, *q = input().split()
    if t == '1':
        rev = 1 - rev
    else:
        num, s = q
        if num == '1':
            if rev:
                S.append(s)
            else:
                S.appendleft(s)
        else:
            if rev:
                S.appendleft(s)
            else:
                S.append(s)

ans = ''.join(S)
print(ans[::-1] if rev else ans)