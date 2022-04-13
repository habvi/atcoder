n = int(input())
S = set([input() for _ in range(n)])

for s in S:
    if ''.join(('!', s)) in S:
        print(s)
        exit()
print('satisfiable')



# from collections import defaultdict

# n = int(input())
# S = set(input() for _ in range(n))

# d = defaultdict(int)
# for s in S:
#     if s[0] == '!':
#         d[s[1:]] |= 2
#     else:
#         d[s] |= 1

# for k, v in d.items():
#     if v == 3:
#         print(k)
#         exit()
# print('satisfiable')