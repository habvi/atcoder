from decimal import Decimal
a, b, c = input().split()
sq = Decimal('0.5')
if Decimal(a) ** sq + Decimal(b) ** sq < Decimal(c) ** sq:
    print('Yes')
else:
    print('No')