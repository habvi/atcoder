from itertools import permutations
from collections import Counter
 
s1 = list(input())
s2 = list(input())
s3 = list(input())
 
c = Counter(s1) + Counter(s2) + Counter(s3)
n = len(c)
if n > 10:
    print('UNSOLVABLE')
    exit()
    
nums = list(c.keys())
d = dict(zip(nums, range(n)))
 
for p in permutations(range(10), n):
    f1 = p[d[s1[0]]]
    f2 = p[d[s2[0]]]
    f3 = p[d[s3[0]]]
    if not f1 or not f2 or not f3:
        continue
    
    t1 = int(''.join([str(p[d[s]]) for s in s1]))
    t2 = int(''.join([str(p[d[s]]) for s in s2]))
    t3 = int(''.join([str(p[d[s]]) for s in s3]))
 
    if t1 > 0 and t2 > 0 and t3 > 0 and t1 + t2 == t3:
        for ans in (t1, t2, t3):
            print(ans)
        exit()
        
print('UNSOLVABLE')