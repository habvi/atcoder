#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    const int n = 1000;
    vector<string> v;
    rep(i, 1, n + 1) {
        v.push_back(to_string(i));
    }

    sort(v.begin(), v.end());
    for (auto &s : v) {
        cout << s << endl;
    }
    return 0;
}