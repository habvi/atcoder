from math import gcd
n = int(input())
A = list(map(int, input().split()))
gl, gr = [], []
l, r = A[0], A[-1]
for i in range(n):
    gl.append(gcd(l, A[i]))
    l = gl[-1]
    gr.append(gcd(r, A[-i - 1]))
    r = gr[-1]
gr = gr[::-1]

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, gr[i + 1])
    elif i == n - 1:
        ans = max(ans, gl[i - 1])
    else:
        ans = max(ans, gcd(gl[i - 1], gr[i + 1]))
print(ans)