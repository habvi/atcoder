# PyPy only

def nmrt():
    return -N * n * h

def dnmnt():
    return N*h + N*n - 4*n*h


N = int(input())
mx = 3501

for h in range(1, mx):
    for n in range(1, mx):
        under = dnmnt()
        if under == 0:
            continue

        top = nmrt()
        w = top // under
        if top % under == 0 and w > 0:
            print(h, n, w)
            exit()