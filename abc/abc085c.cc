#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
    int N, price;
    cin >> N >> price;

    int max_n_10000 = min(price / 10000, N);
    int max_n_5000 = min(price / 5000, N);
    int max_n_1000 = min(price / 1000, N);

    bool valid = false;
    int I = -1;
    int J = -1;
    int K = -1;
    for (int i=0; i<max_n_10000+1; i++) {
        for (int j=0; j<max_n_5000+1; j++) {
            int k = N - i - j;
            if (k >= 0 && k <= max_n_1000 && (i * 10000 + j * 5000 + k * 1000) == price) {
                I = i;
                J = j;
                K = k;
                valid = true;
                break;
            }
            if (valid) break;
        }
        if (valid) break;
    }

    cout << I << " " << J << " " << K << endl;
    return 0;
}