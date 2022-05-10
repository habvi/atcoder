#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    const int m = 3;
    vector<vector<int>> A(m, vector<int>(m));
    rep(i, 0, m) {
        rep(j, 0, m) {
            cin >> A[i][j];
        }
    }

    int n;
    cin >> n;
    set<int> st;
    rep(i, 0, n) {
        int b;
        cin >> b;
        st.insert(b);
    }

    bool ans = false;
    int d1 = 0, d2 = 0;
    rep(i, 0, m) {
        int row = 0, col = 0;
        rep(j, 0, m) {
            row += st.count(A[i][j]);
            col += st.count(A[j][i]);
        }
        ans |= (row == m);
        ans |= (col == m);

        d1 += st.count(A[i][i]);
        d2 += st.count(A[i][m - i - 1]);
        ans |= (d1 == m);
        ans |= (d2 == m);
    }

    cout << (ans ? "Yes" : "No") << endl;

    return 0;
}