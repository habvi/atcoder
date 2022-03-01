a, b = map(int, input().split())
card = list(range(2, 14)) + [1]

if a == b:
    print('Draw')
elif card.index(a) > card.index(b):
    print('Alice')
else:
    print('Bob')