#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int g1(string s) {
    sort(s.rbegin(), s.rend());
    return stoi(s);
}

int g2(string s) {
    sort(s.begin(), s.end());
    return stoi(s);
}

int f(int x) {
    string s = to_string(x);
    return g1(s) - g2(s);
}

int main(void) {
    int n, K;
    cin >> n >> K;

    rep(i, 0, K) {
        n = f(n);
    }

    cout << n << endl;
    return 0;
}