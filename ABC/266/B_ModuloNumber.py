N = int(input())
MOD = 998244353

mod = N % MOD
for i in range(MOD):
    if i % MOD == mod:
        print(i)
        exit()



# ----------------------
N = int(input())
MOD = 998244353

print(N % MOD)
