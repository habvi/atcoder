n = int(input())

a = set()
b = set()
for _ in range(n):
    s = input()
    if s[0] == '!':
        a.add(s[1:])
    else:
        b.add(s)
        
for t in b:
    if t in a:
        print(t)
        exit()
print('satisfiable')