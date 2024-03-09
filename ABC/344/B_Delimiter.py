x = 1
A = []
while x:
    x = int(input())
    A.append(x)
print(*A[::-1])
