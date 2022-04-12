def itos(i):
    return chr(i + ord('a'))

def deci_to_n(x, base):
    x -= 1
    if x >= base:
        yield from deci_to_n(x // base, base)
    yield x % base


n = int(input())

ans = []
for i in deci_to_n(n, 26):
    ans.append(itos(i))
print(''.join(ans))