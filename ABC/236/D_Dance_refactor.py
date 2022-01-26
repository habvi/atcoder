import sys
sys.setrecursionlimit(10**7)

n = int(input())
n2 = 2 * n

A = [[-1] * n2 for _ in range(n2)]
for i in range(n2 - 1):
    A[i][i + 1:] = map(int, input().split())

def dfs(fst, xor, seen):
    if len(seen) == n2:
        global ans
        ans = max(ans, xor)            
        return
    
    if len(seen) % 2:
        for i in range(n2):
            if i not in seen:
                seen.add(i)
                dfs(None, xor ^ A[fst][i], seen)
                seen.remove(i)
    else:
        for i in range(n2):
            if i not in seen:
                seen.add(i)
                dfs(i, xor, seen)
                break
        seen.remove(i)
        
ans = 0
dfs(None, 0, set())
print(ans)