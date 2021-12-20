a, b, c = map(int, input().split())
ans = 0
for i in range(c//a + 1):
    ans = max(ans, i + (c - a*i)//b)
print(ans)

# a, b, c = map(int, input().split())
# print(c // (min(a, b)))