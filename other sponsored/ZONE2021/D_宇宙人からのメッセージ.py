from collections import deque
S = input()
hn = 0
t = deque([])
for s in S:
    if s == 'R':
        hn = 1 - hn
    else:
        if hn:
            if t and t[0] == s:
                t.popleft()
                continue
            t.appendleft(s)
        else:
            if t and t[-1] == s:
                t.pop()
                continue
            t.append(s)
print("".join(list(t)[::-1]) if hn else "".join(list(t)))