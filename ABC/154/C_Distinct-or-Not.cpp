#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    int n;
    cin >> n;

    map<int, int> mp;
    rep(i, 0, n) {
        int a;
        cin >> a;
        if (mp[a]) {
            cout << "NO" << endl;
            return 0;
        } else {
            mp[a] = 1;
        }
    }

    cout << "YES" << endl;
    return 0;
}