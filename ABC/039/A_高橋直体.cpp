#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

int main(void) {
    int A, B, C;
    cin >> A >> B >> C;

    cout << (A * B + B * C + C * A) * 2 << endl;
    return 0;
}