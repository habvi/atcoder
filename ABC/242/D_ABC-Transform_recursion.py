import sys
sys.setrecursionlimit(10 ** 7)

def stoi(s):
    return ord(s) - ord('A')

def nxt(s, t):
    return A[(stoi(s) + t) % 3]

def f(t, k):
    if t == 0:
        return S[k]
    if k == 0:
        return nxt(S[0], t)

    if k % 2:
        return nxt(f(t - 1, k // 2), 2)
    else:
        return nxt(f(t - 1, k // 2), 1)


S = input()
A = 'ABC'

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    k -= 1
    print(f(t, k))