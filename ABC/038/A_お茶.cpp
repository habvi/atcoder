#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

int main(void) {
    string S;
    cin >> S;

    int i = S.size();
    cout << (S[i - 1] == 'T' ? "YES" : "NO") << endl;;
    return 0;
}