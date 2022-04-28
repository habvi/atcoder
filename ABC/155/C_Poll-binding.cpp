#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

int main(){
    int n;
    cin >> n;
    map<string, int> mp;
    rep(i, 0, n) {
        string s;
        cin >> s;
        mp[s]++;
    }

    int mx = 0;
    for (auto x : mp) {
        int num = x.second;
        if (num > mx) {
            mx = num;
        }
    }

    for (auto [name, num] : mp) {
        if (num == mx) {
            cout << name << "\n";
        }
    }

    return 0;
}