#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    int n;
    cin >> n;

    int ans = 0;
    rep(i, 100, 1000) {
        string S = to_string(i);
        int ok = 0;
        for (char c : S) {
            int x = c - '0';
            ok += (1 <= x && x <= n);
        }
        ans += (ok == 3);
    }

    cout << ans << endl;
    return 0;
}


// int main(void) {
//     int n;
//     cin >> n;

//     cout << n * n * n << endl;
//     return 0;
// }