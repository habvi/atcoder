a, b = map(int, input().split())
s = [i for i in range(2, 14)] + [1]
al, bb = s.index(a), s.index(b)

if al == bb: print('Draw')
elif al > bb: print('Alice')
else: print('Bob')