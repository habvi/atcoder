n = int(input())
if n >= 42:
    print('AGC' + '0' * (3 - len(str(n))) + str(n + 1))
else:
    print('AGC' + '0' * (3 - len(str(n))) + str(n))