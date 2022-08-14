from decimal import Decimal, ROUND_DOWN

A, B = map(Decimal, input().split())
ab = A * B
print(ab.quantize(Decimal("0"), rounding=ROUND_DOWN))