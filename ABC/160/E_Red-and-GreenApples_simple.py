x, y, a, b, c = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)

mix = [*P[:x], *Q[:y], *R]
mix.sort(reverse=True)

print(sum(mix[:x + y]))