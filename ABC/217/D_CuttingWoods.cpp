// 2021.10.14

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define _GLIBCXX_DEBUG

int main() {
    int L, Q;
    cin >> L >> Q;
    set<int> st;
    st.insert(0);
    st.insert(L);

    rep(i, Q) {
        int c, x; 
        cin >> c >> x;
        if (c == 1) {
            st.insert(x);
        } else {
            auto it = st.lower_bound(x);
            int r = *it;
            int l = *prev(it);
            cout << r - l << endl;
        }
    }
}