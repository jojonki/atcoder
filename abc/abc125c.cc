#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b) {
    if (a == 0) return b;
    if (b == 0) return a;

    ll quot = a/b;
    ll mod = a%b;
    
    if (mod == 0) {
        return b;
    } else {
        return gcd(b, mod);
    }

}

int main() { 
    int N; cin >> N;
    vector<ll> A;
    for (int i=0; i<N; i++) {
        ll a; cin >> a;
        A.push_back(a);
    }

    vector<ll> left(N+1, 0);
    vector<ll> right(N+1, 0);
    for (int i=0; i<N; i++) {
        left[i+1] = gcd(left[i], A[i]);
    }
    for (int i=N-1; i>=0; i--) {
        right[i] = gcd(right[i+1], A[i]);
    }

    ll maxGcd = 0;
    for (int i=0; i<N; i++) {
        maxGcd = max(maxGcd, gcd(left[i], right[i+1]));
    }

    cout << maxGcd << endl;
    
    return 0;
}