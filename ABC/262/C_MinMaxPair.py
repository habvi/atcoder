N = int(input())
A = list(map(int, input().split()))

same = 0
diff = 0
correct = 0
for i, a in enumerate(A):
    if i + 1 == a:
        same += correct
        correct += 1
    else:
        if A[a - 1] == i + 1:
            diff += 1
print(same + diff // 2)