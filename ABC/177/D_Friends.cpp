#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG
#define rep(i, a, b) for (int i = a; i < b; ++i)

struct UnionFind {
    vector<int> rank;
    UnionFind(int n) : rank(n, -1) { }

    int root(int x) {
        if (rank[x] < 0) {
           return x;
        }
        return rank[x] = root(rank[x]);
    }
    bool unite(int cx, int cy) {
        int x = root(cx), y = root(cy);
        if (x == y) {
            return false;
        }
        if (rank[x] > rank[y]) {
            swap(x, y);
        }
        rank[x] += rank[y];
        rank[y] = x;
        return true;
    }
    bool is_same(int x, int y) {
        return root(x) == root(y);
    }
    int st_size(int x) {
        return -rank[root(x)];
    }
};

int main(void) {
    int n, m;
    cin >> n >> m;

    UnionFind uf(n);
    while (m--) {
        int a, b;
        cin >> a >> b;
        uf.unite(a - 1, b - 1);
    }

    int ans = 0;
    rep(i, 0, n) {
        if (i == uf.root(i)) {
            ans = max(ans, uf.st_size(i));
        }
    }
    cout << ans << endl;
    return 0;
}