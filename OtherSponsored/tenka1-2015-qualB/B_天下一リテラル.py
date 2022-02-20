S = input()

if S == '{}':
    print('dict')
    exit()

par = 0
for s in S:
    if s == '{':
        par += 1
        continue
    if s == '}':
        par -= 1
        continue

    if par == 1:
        if s == ':':
            print('dict')
            exit()
        elif s == ',':
            print('set')
            exit()

print('set')