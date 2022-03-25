S = list(input().split())
n = int(input())
NG = [input() for _ in range(n)]

for word in S:
    ok = False
    for ng in NG:
        if len(word) != len(ng):
            continue

        same = False
        for a, b in zip(word, ng):
            if b != '*' and a != b:
                break
        else:
            same = True

        ok |= same

    print('*' * len(word) if ok else word)