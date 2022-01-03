# flushなしでもokだった

import sys
n = int(input())
mx = -1
for i in range(2, n + 1): 
    print(f"? {1} {i}")
    sys.stdout.flush()
    dist = int(input())
    if mx < dist:
        mx = dist
        mv = i

ans = 0
for i in range(1, n + 1):
    if i == mv:
        continue 
    print(f"? {mv} {i}")
    sys.stdout.flush()
    ans = max(ans, int(input()))
print('!', ans)