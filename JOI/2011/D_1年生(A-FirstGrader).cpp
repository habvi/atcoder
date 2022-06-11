#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    int n;
    cin >> n;
    vector<int> A(n);
    rep(i, 0, n) {
        cin >> A[i];
    }

    int last = A[n - 1];
    const int mx = 20;
    vector<long long> dp(mx + 1, 0);
    dp[A[0]] = 1;

    rep(i, 1, n - 1) {
        int now = A[i];
        vector<long long> ndp(mx + 1, 0);
        rep(pre, 0, mx + 1) {
            int total = pre + now;
            if (0 <= total && total <= mx) {
                ndp[total] += dp[pre];
            }
            int total2 = pre - now;
            if (0 <= total2 && total2 <= mx) {
                ndp[total2] += dp[pre];
            }
        }
        dp = ndp;
    }

    cout << dp[last] << endl;
    return 0;
}