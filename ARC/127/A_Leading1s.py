s = input()
n = int(s)
ln = len(s)
ans = 1
if n < 2*10**(ln-1) - 1:
    for i in range(2, ln):
        ans += i
        for j in range(1, i):
            ans += j * 9 * 10**(i - j - 1)

    comp = []
    b = 0
    for i in range(ln):
        b |= 1 << ln-i-1
        comp.append((int(bin(b)[2:]), i + 1))

    plus = [1, 8]
    for i in range(ln - 3):
        plus.append(plus[-1] * 10)
    for i, p in enumerate(plus):
        comp.append((comp[-1][0] + p, ln - i - 1))
    comp.append((comp[0][0] * 2, 0))

    for i in range(len(comp) - 1):
        c, num = comp[i]
        c2, num2 = comp[i + 1]
        if n <= c2 - 1:
            ans += (n - c + 1)*num
            break
        ans += (c2 - c)*num
else:
    for i in range(2, ln + 1):
        ans += i
        for j in range(1, i):
            ans += j * 9 * 10**(i - j - 1)    
print(ans)