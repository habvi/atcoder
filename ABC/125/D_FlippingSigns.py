n = int(input())
A = list(map(int, input().split()))

minus = sum(a < 0 for a in A)

B = [abs(a) for a in A]
total = sum(B)

if minus % 2:
    print(total - min(B) * 2)
else:
    print(total)