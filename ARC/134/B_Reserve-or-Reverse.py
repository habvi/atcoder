from collections import defaultdict

n = int(input())
S = input()
T = list(S)

d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)

mx = n - 1
for i, s in enumerate(S):
    if mx <= i:
        break
    
    for al in range(ord('a'), ord('z') + 1):
        if al >= ord(s):
            break
        if chr(al) not in d:
            continue

        while d[chr(al)] and d[chr(al)][-1] > mx:
            d[chr(al)].pop()
        if not d[chr(al)]:
            del d[chr(al)]
            continue
        
        idx = d[chr(al)][-1]
        d[chr(al)].pop()
        if not d[chr(al)]:
            del d[chr(al)]
            
        if idx <= i:
            continue
        
        T[idx], T[i] = T[i], T[idx]
        mx = idx
        break
print(''.join(T))