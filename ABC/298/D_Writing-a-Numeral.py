from collections import deque

Q = int(input())
MOD = 998244353
dq = deque(['1'])
num = 1
digit = 1
for _ in range(Q):
    q, *x = map(int, input().split())
    if q == 1:
        x = x[0]
        dq.append(str(x))
        num = num * 10 + x
        num %= MOD
        digit += 1
    elif q == 2:
        head = dq.popleft()
        digit -= 1
        num -= int(head) * pow(10, digit, MOD)
    else:
        print(num % MOD)