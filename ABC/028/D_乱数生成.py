n, k = map(int, input().split())
sm = n * n * n
less, large = k - 1, n - k
a = 6 * less * large + 3 * (less + large) + 1
print(a / sm)