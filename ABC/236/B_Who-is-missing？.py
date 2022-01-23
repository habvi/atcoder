from collections import Counter

n = int(input())
A = list(map(int, input().split()))

for k, v in Counter(A).items():
    if v == 3:
        print(k)
        exit()