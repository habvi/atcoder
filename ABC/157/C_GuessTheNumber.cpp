#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    int n, m;
    cin >> n >> m;

    vector<int> num(n, -1);
    rep(i, 0, m) {
        int s, c;
        cin >> s >> c;
        s--;
        if (num[s] == -1) {
            num[s] = c;
        } else if (num[s] != c) {
            cout << -1 << endl;
            return 0;
        }
    }

    if (n > 1) {
        if (num[0] == -1) {
            num[0] = 1;
        } else if (num[0] == 0) {
            cout << -1 << endl;
            return 0;
        }
    }

    int ans = 0;
    double k = pow(10, n - 1);
    for (auto &x : num) {
        if (x != -1) {
            ans += x * k;
        }
        k /= 10;
    }

    cout << ans << endl;
    return 0;
}