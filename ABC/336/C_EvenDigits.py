N = int(input())

if N == 1:
    print(0)
    exit(0)

N -= 1
digits = "02468"
base5 = []
while N > 0:
    base5.append(N % 5)
    N //= 5

s = [digits[b] for b in reversed(base5)]
print("".join(s))
