def ceil(a, b):
    return (a + b - 1) // b


A, B, W = map(int, input().split())

W *= 1000
mn = ceil(W, B)
mx = W // A
if mn <= mx:
    print(mn, mx)
else:
    print("UNSATISFIABLE")



# ------------------------
a, b, w = map(int, input().split())

w *= 1000
m = []
for i in range(w//b - 5, w//a + 5):
    if i == 0:
        continue
    if a <= w / i <= b:
        m.append(i)

if m:
    print(min(m), max(m))
else:
    print("UNSATISFIABLE")