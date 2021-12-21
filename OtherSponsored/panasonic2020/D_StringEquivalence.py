import sys
sys.setrecursionlimit(10**7)

def dfs(s, mx):
    if len(s) == n:
        print(s)
        return
    for i in range(ord('a'), ord(mx) + 1):
        if chr(i) == mx:
            mx = chr(ord(mx) + 1)
        dfs(s + chr(i), mx)

n = int(input())
dfs("", 'a')