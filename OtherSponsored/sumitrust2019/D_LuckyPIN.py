n = int(input())
S = input()

one = set()
two = set()
three = set()
for s in S:
    for t in two:
        three.add(t + s)
        
    for t in one:
        two.add(t + s)
    
    one.add(s)
print(len(three))