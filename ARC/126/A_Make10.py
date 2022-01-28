T = int(input())
for _ in range(T):
    n2, n3, n4 = map(int, input().split())
    ans = 0
    
    a = min(n3 // 2, n4)
    ans += a
    n3 -= a * 2
    n4 -= a
    
    a = min(n2 // 2, n3 // 2)
    ans += a
    n2 -= a * 2
    n3 -= a * 2
    
    a = min(n2, n4 // 2)
    ans += a
    n2 -= a
    n4 -= a * 2
    
    a = min(n2 // 3, n4)
    ans += a
    n2 -= a * 3
    n4 -= a
    
    ans += n2 // 5
    print(ans)