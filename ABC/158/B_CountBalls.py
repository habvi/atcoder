n, a, b = map(int, input().split())

ab = a + b
ans = n//ab * a + min(n % ab, a)

print(ans)



# n, a, b = map(int, input().split())

# ab = a + b
# ans = n//ab * a

# if n % ab <= a:
#     ans += n % ab
# else:
#     ans += a
# print(ans)