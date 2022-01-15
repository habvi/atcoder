n = int(input())
h = list(map(int, input().split()))
a = h[0]
for i in range(1, n):
    if h[i] <= a:
        print(h[i - 1])
        exit()
    a = h[i]
print(a)