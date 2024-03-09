_ = int(input())
A = sorted(map(int, input().split()))
_ = int(input())
B = sorted(map(int, input().split()))
_ = int(input())
C = sorted(map(int, input().split()))
_ = int(input())
X = list(map(int, input().split()))

s = []
for a in A:
    for b in B:
        for c in C:
            s.append(a + b + c)

s = set(s)
for x in X:
    print("Yes" if x in s else "No")
