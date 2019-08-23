#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() { 
    int N, K;
    cin >> N >> K;

    double p = 0;

    if (N-K+1>=0) {
        p += (double)(N-K+1)/N;
    }
    for (int i=1; i<=N; i++) {
        if (i>=K) break;
        int n = ceil(log2((double)K/i));
        // cout << n << endl;
        p += (double)1.0/N * pow(double(0.5), n);
    }

    cout << fixed << setprecision(10) << p << endl;

    return 0;
}