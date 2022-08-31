from collections import deque

def head(x):
    tmp = []
    for _ in range(x):
        tmp.append(q.popleft())
    print(q.popleft())
    for t in tmp[::-1]:
        q.appendleft(t)

def tail(x):
    tmp = []
    for _ in range(x):
        tmp.append(q.pop())
    print(q.pop())
    for t in tmp[::-1]:
        q.append(t)


N = int(input())
S = input()

q = deque([])
for i, s in enumerate(S, 1):
    x = -1
    if s == 'L':
        q.appendleft(i)
    elif s == 'R':
        q.append(i)
    elif s in "AD":
        x = 0
    elif s in "BE":
        x = 1
    elif s in "CF":
        x = 2

    if x >= 0:
        if len(q) <= x:
            print("ERROR")
        else:
            if s in "ABC":
                head(x)
            else:
                tail(x)