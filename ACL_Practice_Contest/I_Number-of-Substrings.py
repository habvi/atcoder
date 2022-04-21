def sa_is(S, upper):
    n = len(S)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        if (S[0] < S[1]):
            return [0, 1]
        else:
            return [1, 0]

    sa = [0] * n
    ls = [0] * n
    for i in range(n - 2, -1, -1):
        ls[i] = ls[i + 1] if (S[i] == S[i + 1]) else (S[i] < S[i + 1])

    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if not ls[i]:
            sum_s[S[i]] += 1
        else:
            sum_l[S[i] + 1] += 1
    for i in range(upper + 1):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]

    def induce(lms):
        for i in range(n):
            sa[i] = -1
        buf = sum_s[:]
        for d in lms:
            if d == n:
                continue
            sa[buf[S[d]]] = d
            buf[S[d]] += 1
        buf = sum_l[:]
        sa[buf[S[n - 1]]] = n - 1
        buf[S[n - 1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v - 1]:
                sa[buf[S[v - 1]]] = v - 1
                buf[S[v - 1]] += 1
        buf = sum_l[:]
        for i in range(n - 1, -1, -1):
            v = sa[i]
            if v >= 1 and ls[v - 1]:
                buf[S[v - 1] + 1] -= 1
                sa[buf[S[v - 1] + 1]] = v - 1
    lms_map = [-1] * (n + 1)
    m = 0
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            m += 1
    lms = []
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms.append(i)
    induce(lms)

    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            l = sorted_lms[i - 1]
            r = sorted_lms[i]
            end_l = lms[lms_map[l] + 1] if (lms_map[l] + 1 < m) else n
            end_r = lms[lms_map[r] + 1] if (lms_map[r] + 1 < m) else n
            same = True
            if end_l - l != end_r - r:
                same = False
            else:
                while l < end_l:
                    if S[l] != S[r]:
                        break
                    l += 1
                    r += 1
                if (l == n) or (S[l] != S[r]):
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper
        rec_sa = sa_is(rec_s, rec_upper)
        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]
        induce(sorted_lms)
    return sa

def suffix_array(S):
    n = len(S)
    if type(S) == str:
        s2 = [ord(s) for s in S]
        return sa_is(s2, 255)
    else:
        idx = list(range(n))
        idx.sort(key=lambda x : S[x])
        s2 = [0] * n
        now = 0
        for i in range(n):
            if (i & S[idx[i - 1]] != S[idx[i]]):
                now += 1
            s2[idx[i]] = now
        return sa_is(s2, now)

def lcp_array(S, sa):
    n = len(S)
    assert n >= 1
    rnk = [0] * n
    for i in range(n):
        rnk[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i] - 1]
        while(j + h < n) and (i + h < n):
            if S[j + h] != S[i + h]:
                break
            h += 1
        lcp[rnk[i] - 1] = h
    return lcp


S = input()
n = len(S)

suffix = suffix_array(S)
lcp = lcp_array(S, suffix)
print(n * (n + 1) // 2 - sum(lcp))