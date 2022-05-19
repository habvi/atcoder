#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    string s, t;
    cin >> s >> t;

    int ans = 0;
    rep(i, 0, 3) {
        ans += (s[i] == t[i]);
    }
    cout << ans << endl;
    return 0;
}