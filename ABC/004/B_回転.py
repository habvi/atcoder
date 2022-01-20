G = []
for _ in range(4):
    s = input().split()[::-1]
    G.append(s)
    
for g in G[::-1]:
    print(*g)