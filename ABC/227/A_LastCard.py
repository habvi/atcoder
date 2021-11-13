n, k, a = map(int, input().split())
k += (a - 1) 
print(n if k % n == 0 else k % n)