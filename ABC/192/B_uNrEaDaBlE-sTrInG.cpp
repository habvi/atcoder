#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    string S;
    cin >> S;

    rep(i, 0, S.size()) {
        char c =  S[i];
        if (!(i % 2 == 0 && islower(c) || i % 2 && isupper(c))) {
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;
    return 0;
}