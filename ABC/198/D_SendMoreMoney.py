from itertools import permutations
s1 = input()
s2 = input()
s3 = input()
s = set(s1 + s2 + s3)
if len(s) > 10:
    print('UNSOLVABLE')
    exit()

d = {ss : i for i, ss in enumerate(s)}
for pr in permutations((i for i in range(10)), len(d)):
    if pr[d[s1[0]]] == 0 or pr[d[s2[0]]] == 0 or pr[d[s3[0]]] == 0:
        continue
    t1 = [str(pr[d[s]]) for s in s1]
    t2 = [str(pr[d[s]]) for s in s2]
    t3 = [str(pr[d[s]]) for s in s3]
    j1 = "".join(t1)
    j2 = "".join(t2)
    j3 = "".join(t3)
    if int(j1) + int(j2) == int(j3):
        print(j1)
        print(j2)
        print(j3)
        exit()
print('UNSOLVABLE')

'''
send
more
money
'''