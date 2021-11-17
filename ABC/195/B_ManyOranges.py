a, b, w = map(int, input().split())
w *= 1000
m = []
for i in range(w//b - 5, w//a + 5):
    if i == 0: continue
    if a <= w/i <= b:
        m.append(i)

if m:
    print(min(m), max(m))
else:
    print("UNSATISFIABLE")