T = int(input())

for _ in range(T):
    a, s = map(int, input().split())
    if a * 2 > s:
        print('No')
        continue

    x = s - a * 2
    print('No' if x & a else 'Yes')