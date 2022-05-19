#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    int n;
    cin >> n;
    vector<tuple<int, int>> A;
    rep(i, 0, n) {
        int a;
        cin >> a;
        A.push_back(make_tuple(i, a));
    }

    deque<int> q;
    for (auto &[i, a] : A) {
        if (n % 2 == i % 2) {
            q.push_back(a);
        } else {
            q.push_front(a);
        }
    }

    for (auto &x: q) {
        cout << x << " ";
    }
    cout << endl;
}