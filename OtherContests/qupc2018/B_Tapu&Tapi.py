def solve():
    a, b, c = map(int, input().split())
    if a % 2 == 0:
        if b % 2 == 0:
            return c % 2 == 0
        else:
            if c % 2:
                return  False
            else:
                return c >= 10
    else:
        for i in range(min(11, b + 1)):
            for j in range(min(101, c + 1)):
                if 10*i + j == 100 and (b - i) % 2 == (c - j) % 2 == 0:
                    return True
        return False


q = int(input())
for _ in range(q):
    print('Yes' if solve() else 'No')