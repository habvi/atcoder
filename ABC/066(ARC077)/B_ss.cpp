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



// ----------
#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(void) {
    string s;
    cin >> s;
 
    s.pop_back();
    s.pop_back();
    int n = s.size();
    while (n >= 2) {
        int mid = n / 2;
        string l = s.substr(0, mid), r = s.substr(mid, mid);
        if (l == r) {
            cout << n << endl;
            return 0;
        }
        s.pop_back();
        s.pop_back();
        n -= 2;
    }
}