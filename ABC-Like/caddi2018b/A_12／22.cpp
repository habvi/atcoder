#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    string S;
    cin >> S;

    int ans = 0;
    for (auto &s : S) {
        ans += (s == '2');
    }

    cout << ans << endl;
    return 0;
}