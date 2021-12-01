from decimal import Decimal, ROUND_HALF_UP

d, w = input().split()
d = int(d) / Decimal('10')
w = Decimal(w) / Decimal('60')
w = Decimal(str(w)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

S = ''
if d < Decimal('11.25') or d >= Decimal('348.75'):
    S = 'N'
else:
    for k, s in zip([326.25, 303.75, 281.25, 258.75, 236.25, 213.75, 191.25, 168.75, 146.25, 123.75, 101.25, 78.75, 56.25, 33.75, 11.25], ['NNW', 'NW', 'WNW', 'W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE', 'E', 'ENE', 'NE', 'NNE']):
        if d >= Decimal(str(k)):
            S = s
            break

if w >= Decimal('32.7'):
    print(S, 12)
    exit()

if w <= Decimal('0.2'):
    print('C', 0)
    exit()

for ms, pw in zip([1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6], [i for i in range(1, 12)]):
    if w <= Decimal(str(ms)):
        print(S, pw)
        exit()