#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

int main(void) {
    int r, g, b;
    cin >> r >> g >> b;

    int total = 100 * r + 10 * g + b;
    cout << (total % 4 == 0 ? "YES" : "NO") << endl;

    return 0;
}