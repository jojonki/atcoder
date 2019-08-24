#include <iostream>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;

vector<ll> dp;
vector<int> A;

ll rec(ll i) {
    if (i==0) return dp[0]=0;
    if (dp[i] < LINF) return dp[i];

    ll cost = LINF;
    chmin(cost, rec(i-1) + abs(A[i]-A[i-1]));
    if (i>1) {
        chmin(cost, rec(i-2) + abs(A[i]-A[i-2]));
    }
    return dp[i]=cost;
}

int main() {
    int N; cin >> N;
    A.resize(N, 0);
    REP(i, N) cin >> A[i];
    dp.resize(N, LINF);

    cout << rec(N-1) << endl;
    
    return 0;
}