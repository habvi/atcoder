S = set(input())

for i in range(10):
    if str(i) not in S:
        print(i)
        exit()