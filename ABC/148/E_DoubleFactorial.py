n = int(input())
if n % 2:
    print(0)
    exit()

a = 50
five = [a]
for i in range(25):
    a *= 5
    five.append(a)

ans = 0
for f in five:
    ans += n // f
print(n //10 + ans)