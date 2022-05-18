#include <bits/stdc++.h>
using namespace std;
#define _GLIBCXX_DEBUG

int main(void) {
    int a, b;
    cin >> a >> b;

    if (a + b == 15) {
        cout << "+" << endl;
    } else if (a * b == 15) {
        cout << "*" << endl;
    } else {
        cout << "x" << endl;
    }
    return 0;
}