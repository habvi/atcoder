N = int(input())

x = hex(N)[2:]
ans = '0' * (2 - len(x)) + x.upper()
print(ans)
