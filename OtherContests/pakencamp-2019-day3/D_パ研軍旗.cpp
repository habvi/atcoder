#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    int n;
    cin >> n;
    // red, blue, white
    vector<vector<int>> num(n, vector<int>(3, 0));
    rep(_, 0, 5) {
        string s;
        cin >> s;
        rep(i, 0, n) {
            if (s[i] == 'R') {
                num[i][0] += 1;
            } else if (s[i] == 'B') {
                num[i][1] += 1;
            } else if (s[i] == 'W') {
                num[i][2] += 1;
            }
        }
    }

    const int INF = 1001001001;
    vector<int> dp(3, INF);
    rep(i, 0, 3) {
        dp[i] = 5 - num[0][i];
    }

    rep(i, 1, n) {
        vector<int> ndp(3, INF);
        rep(pre, 0, 3) {
            rep(now, 0, 3) {
                if (pre == now) {
                    continue;
                }
                ndp[now] = min(ndp[now], dp[pre] + 5 - num[i][now]);
            }
        }
        dp = ndp;
    }

    int ans = INF;
    rep(i, 0, 3) {
        ans = min(ans, dp[i]);
    }
    cout << ans << endl;
    return 0;
}