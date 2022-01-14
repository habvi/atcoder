n = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
ans = 0
ii, jj = 0, 0
for a in A:
    for i in range(ii, n):
        if B[i] > a:
            ii = i + 1
            for j in range(jj, n):
                if C[j] > B[i]:
                    ans += 1
                    jj = j + 1
                    break
            else:
                print(ans)
                exit()
            break
    else:
        print(ans)
        exit()
print(ans)