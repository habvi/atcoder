from collections import defaultdict

n = int(input())
S = input()

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)

ans = list(S)
mx = n - 1
for i, s in enumerate(S):
    if mx <= i:
        break
    
    for al in range(ord('a'), ord('z') + 1):
        minc = chr(al)
        if minc >= s:
            break
        if minc not in d:
            continue

        while d[minc] and d[minc][-1] > mx:
            d[minc].pop()
        if not d[minc]:
            del d[minc]
            continue
        
        swap = d[minc][-1]
        d[minc].pop()
        if not d[minc]:
            del d[minc]
            
        if swap <= i:
            continue
        
        ans[i], ans[swap] = ans[swap], ans[i]
        mx = swap
        break
print(''.join(ans))