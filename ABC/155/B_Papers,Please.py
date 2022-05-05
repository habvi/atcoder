from xmlrpc.client import FastMarshaller


n = int(input())
A = list(map(int, input().split()))

for a in A:
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            continue
        print('DENIED')
        exit()
print('APPROVED')