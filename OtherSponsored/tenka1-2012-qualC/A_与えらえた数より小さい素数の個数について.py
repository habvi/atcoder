def furui(x):
    memo = [0]*(x+1)
    primes = []
    for i in range(2, x+1):
        if memo[i]: continue
        primes.append(i)
        memo[i] = i
        for j in range(i*i, x+1, i):
            if memo[j]: continue
            memo[j] = i
    return primes

n = int(input())
primes = furui(n - 1)
print(len(primes))