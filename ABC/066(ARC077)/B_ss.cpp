#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

int main(void) {
    string s;
    cin >> s;

    int n = s.size();
    for (int i = n - 1; i >= 2; --i) {
        if (i % 2) {
            continue;
        }
        int mid = i / 2;
        string l = s.substr(0, mid), r = s.substr(mid, mid);
        if (l == r) {
            cout << i << endl;
            return 0;
        }
    }
}