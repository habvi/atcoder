from itertools import combinations

H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for h in combinations(range(H), H2):
    for w in combinations(range(W), W2):
        C = []
        for i in h:
            c = []
            for j in w:
                c.append(A[i][j])
            C.append(c)
        if B == C:
            print("Yes")
            exit()
print("No")
