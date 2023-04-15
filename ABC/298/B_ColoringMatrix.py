def r_rotate(G):
    return [tuple(reversed(g)) for g in zip(*G)]


N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]

def check(A):
    for i in range(N):
        for j in range(N):
            if not A[i][j]:
                continue
            if not B[i][j]:
                return False
    return True

for _ in range(4):
    A = r_rotate(A)
    if check(A):
        print("Yes")
        exit()
print("No")