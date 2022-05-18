#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    int n, m;
    cin >> n >> m;

    vector<int> pre;
    rep(i, 0, n) {
        vector<int> B(m);
        rep(j, 0, m) {
            cin >> B[j];
        }

        if (i == 0) {
            int head = B[0] % 7;
            if (head == 0) {
                head = 7;
            }
            if (head + m - 1 > 7) {
                cout << "No" << endl;
                return 0;
            }

            vector<int> cmp(m);
            rep(k, 0, m) {
                cmp[k] = B[0] + k;
            }
            if (B != cmp) {
                cout << "No" << endl;
                return 0;
            }
            pre = B;
            continue;
        }

        rep(j, 0, m) {
            if (pre[j] + 7 != B[j]) {
                cout << "No" << endl;
                return 0;
            }
        }
        pre = B;
    }

    cout << "Yes" << endl;
    return 0;
}