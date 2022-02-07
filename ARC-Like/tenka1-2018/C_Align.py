from collections import deque

def make_seq(A):
    da = deque(A)
    q = deque([da.popleft()])
    front = 0
    while da:
        if len(da) == 1:
            num = da.pop()
            if abs(num - q[0]) > abs(num - q[-1]):
                q.appendleft(num)
            else:
                q.append(num)
            break

        if front:
            q.appendleft(da.popleft())
            q.append(da.popleft())
        else:
            q.appendleft(da.pop())
            q.append(da.pop())

        front = 1 - front
    return list(q)


n = int(input())
A = [int(input()) for _ in range(n)]
A.sort()

B = make_seq(A)
ans = 0
for a, b in zip(B, B[1:]):
    ans += abs(a - b)

C = make_seq(A[::-1])
ans2 = 0
for a, b in zip(C, C[1:]):
    ans2 += abs(a - b)

print(max(ans, ans2))