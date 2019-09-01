#include <iostream>
#include <algorithm>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll LINF = 1e18;
const ll INF = 1e9;
using namespace std;

ll gcd(ll A, ll B) {
    ll rem;
    if(A<B) {
        ll tmp = A;
        A = B;
        B = tmp;
    }
    rem = A % B;
    if (rem == 0) {
        return B;
    }

    return gcd(B, rem);
}

int main() { 
    ll N; cin >> N;
    int a1, a2; cin >> a1 >> a2;
    ll g = gcd(a1, a2);
    REP(i, N-2) {
        int a; cin >> a;
        g = gcd(g, a);
    }

    cout << g << endl;

    return 0;
}