n, A, B = map(int, input().split())
S = input()

passed = 0
b = 0
for s in S:
    ans = None
    if s == 'a':
        ans = passed < A + B
        passed += 1
    elif s == 'b':
        b += 1
        ans = passed < A + B and b <= B
        if ans:
            passed += 1
    else:
        ans = False

    print('Yes' if ans else 'No')