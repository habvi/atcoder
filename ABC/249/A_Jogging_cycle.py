from itertools import cycle

def calc(A, x):
    times = 0
    for i, time in enumerate(cycle(A)):
        if x == 0:
            break
        if i % 2 == 0:
            move = min(x, time)
            rest = 0
        else:
            move = 0
            rest = min(x, time)
        x -= move
        x -= rest
        times += move
    return times


a, b, c, d, e, f, X = map(int, input().split())

dt = calc([a, c], X) * b
da = calc([d, f], X) * e

if dt == da:
    print('Draw')
elif dt > da:
    print('Takahashi')
else:
    print('Aoki')