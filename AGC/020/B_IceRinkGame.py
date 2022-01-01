k = int(input())
A = list(map(int, input().split()))
mn, mx = 2, 2
for a in reversed(A):
    mn = (mn + a - 1)//a * a
    mx = (mx - mx%a)//a * a + a - 1
if mn > mx:
    print(-1)
else:
    print(mn, mx)