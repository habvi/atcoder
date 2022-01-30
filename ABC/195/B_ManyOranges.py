a, b, kg = map(int, input().split())
g = 1000 * kg

mn = (g + b - 1) // b
mx = g // a
if mn <= mx:
    print(mn, mx)
else:
    print('UNSATISFIABLE')