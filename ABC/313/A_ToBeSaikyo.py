N = int(input())
P = list(map(int, input().split()))

mx = max([0, *P[1:]]) + 1
print(max(0, mx - P[0]))