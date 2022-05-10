#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

int main(void) {
    int n;
    cin >> n;

    int mn = 1000, mx = 0;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        mn = min(mn, a);
        mx = max(mx, a);
    }

    cout << mx - mn << endl;

    return 0;
}