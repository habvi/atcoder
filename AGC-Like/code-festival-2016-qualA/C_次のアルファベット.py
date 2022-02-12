S = input()
K = int(input())

ans = []
for s in S:
    if s == 'a':
        ans.append('a')
        continue
    
    res = ord('z') - ord(s) + 1
    if res <= K:
        ans.append('a')
        K -= res
    else:
        ans.append(s)

if K:
    ans[-1] = chr((ord(ans[-1]) - ord('a') + K) % 26 + ord('a'))

print(''.join(ans))