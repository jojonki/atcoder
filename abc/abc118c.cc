#include <iostream>
#include <algorithm>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll LINF = 1e18;
const ll INF = 1e9;
using namespace std;

ll rec(vector<ll> &A, ll idx) {
    sort(A.begin(), A.end());
    ll mn=0;
    for(ll i=idx; i<A.size(); i++) {
        if(A[i]!=0) {
            if(A[i] == 1) {
                return 1;
            } else {
                idx = i;
                mn = A[i];
                break;
            }
        }
    }

    if (idx == A.size()-1 || mn==0) {
        return mn;
    }

    for(ll i=idx+1; i<A.size(); i++) {
        A[i] %= mn;
    }

    return rec(A, idx);
}

int main() { 
    ll N; cin >> N;
    vector<ll> A;
    REP(i, N) {
        int a; cin >> a;
        A.push_back(a);
    }

    cout << rec(A, 0) << endl;

    return 0;
}