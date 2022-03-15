def f(i):
    return r * A[i] - D 

r, D, x = map(int, input().split())
A = [x]

for i in range(10):
    res = f(i)
    A.append(res)
    print(res)