from datetime import date, timedelta
y, m, d = map(int, input().split('/'))

def ok(y, m, d):
    return y % m == 0 and y // m % d == 0
    
while not ok(y, m, d):
    dt = date(y, m, d) + timedelta(days=1)
    y, m, d = dt.year, dt.month, dt.day

def zero(x):
    return '0' * (2 - len(str(x))) + str(x)

print(f'{y}/{zero(m)}/{zero(d)}')