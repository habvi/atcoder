n = int(input())
S = set([input() for _ in range(n)])
        
for s in S:
    if ''.join(('!', s)) in S:
        print(s)
        exit()
print('satisfiable')