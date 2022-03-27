import sys
sys.setrecursionlimit(10 ** 7)

def solve(s, mx):
    if len(s) == n:
        print(s)
        return

    for i in range(mx + 1):
        solve(s + chr(ord('a') + i), max(mx, i + 1))


n = int(input())
solve('', 0)