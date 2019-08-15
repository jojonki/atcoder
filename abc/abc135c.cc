#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
typedef long long ll;

int main()
{
    int N;
    cin >> N;
    vector<ll> A, B;
    int nA = N+1;
    int nB = N;
    while(nA--) {
        ll a;
        cin >> a;
        A.push_back(a);
    }
    while(nB--) {
        ll b;
        cin >> b;
        B.push_back(b);
    }

    ll nm = 0;
    for (int i=0; i<N; i++) {
        int hit = min(A[i], B[i]);;
        // A[i] -= hit;
        B[i] -= hit;
        nm += hit;

        hit = min(A[i+1], B[i]);
        A[i+1] -= hit;
        // B[i] -= hit;
        nm += hit;
    }

    cout << nm << endl;

    return 0;
}