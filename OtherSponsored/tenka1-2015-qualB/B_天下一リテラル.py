S = input()
if S == '{}':
    print('dict')
    exit()
    
cnt = 0
for s in S:
    if s == '{':
        cnt += 1
        continue
    if s == '}':
        cnt -= 1
        continue
    if cnt == 1:
        if s == ':':
            print('dict')
            exit()
        if s == ',':
            print('set')
            exit()
print('set')