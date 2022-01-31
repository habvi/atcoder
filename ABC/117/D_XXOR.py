n, k = map(int, input().split())
A = list(map(int, input().split()))

lenk = len(bin(k)) - 2

zero = False
ans = k
for i in reversed(range(lenk)):
    bit = 0
    for a in A:
        bit += a >> i & 1
    
    if bit > n // 2 and k >> i & 1:
        ans ^= 1 << i
        zero = True
        continue
    
    if (bit <= n // 2) and (not k >> i & 1) and zero:
        ans |= 1 << i

print(sum(ans ^ a for a in A))