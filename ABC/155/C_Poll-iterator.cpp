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

    for (auto itr = mp.begin(); itr != mp.end(); itr++) {
        if (itr->second == mx) {
            cout << itr->first << "\n";
        }
    }

    return 0;
}