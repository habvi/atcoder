#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)
using ll = long long;

int main(void) {
    int N, M;
    cin >> N >> M;
    ll A, B, C, D, E, F;
    cin >> A >> B >> C >> D >> E >> F;
    set<pair<ll, ll>> s;
    rep(_, 0, M) {
        ll x, y;
        cin >> x >> y;
        s.insert({x, y});
    }
    const int MOD = 998244353;

    map<pair<ll, ll>, int> dp;
    dp[{0, 0}] = 1;
    rep(_, 0, N) {
        map<pair<ll, ll>, int> ndp;
        for (auto [k, v] : dp) {
            ll x = k.first;
            ll y = k.second;
            ll nx = x + A;
            ll ny = y + B;
            if (!s.count({nx, ny})) {
                ndp[{nx, ny}] += v;
                ndp[{nx, ny}] %= MOD;
            }
            nx = x + C;
            ny = y + D;
            if (!s.count({nx, ny})) {
                ndp[{nx, ny}] += v;
                ndp[{nx, ny}] %= MOD;
            }
            nx = x + E;
            ny = y + F;
            if (!s.count({nx, ny})) {
                ndp[{nx, ny}] += v;
                ndp[{nx, ny}] %= MOD;
            }
        }
        swap(dp, ndp);
    }

    ll ans = 0;
    for (auto [k, v] : dp) {
        ans += v;
        ans %= MOD;
    }
    cout << ans << endl;
    return 0;
}
