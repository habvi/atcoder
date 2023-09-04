from heapq import heappop, heappush

N, K = map(int, input().split())
A = list(map(int, input().split()))

octp = []
hq = [0]
used = set()
while len(octp) <= K:
    total = heappop(hq)
    for a in A:
        new_total = total + a
        if new_total in used:
            continue
        heappush(hq, new_total)
        used.add(new_total)
    octp.append(total)

print(octp[K])
