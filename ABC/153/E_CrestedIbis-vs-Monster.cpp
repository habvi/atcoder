#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

const int INF = 1001001001;

int main(void) {
    int h, n;
    cin >> h >> n;

    vector<int> dp(h + 1, INF);
    dp[0] = 0;
    rep(_, 0, n) {
        int a, b;
        cin >> a >> b;

        rep(i, 0, h + 1) {
            int j;
            j = min(i + a, h);
            dp[j] = min(dp[j], dp[i] + b);
        }
    }

    cout << dp[h] << endl;
    return 0;
}