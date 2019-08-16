#include <iostream>
using namespace std;

int main() {
    int N, L;
    cin >> N >> L;

    int sumt = 0;
    int mint = 100;
    for (int i=1; i<=N; i++) {
        int t = (L + i - 1);
        if (abs(t) < abs(mint)) {
            mint = t;
        }
        sumt += t;
    }

    cout << (sumt - mint) << endl;

    return 0;
}