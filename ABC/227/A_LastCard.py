n, k, a = map(int, input().split())
k += (a - 1) 
print(n if k % n == 0 else k % n)



# n, k, a = map(int, input().split())
# print((a - 1 + k - 1) % n + 1)