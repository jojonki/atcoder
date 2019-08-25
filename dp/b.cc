#include <iostream>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;

vector<ll> dp;
vector<int> H;

ll rec(int i, int K) {
    if (i==0) return dp[0] = 0;
    if (dp[i] < LINF) return dp[i];

    ll cost = LINF;
    for(int k=1; k<K+1; k++) {
        if(i>=k) {
            chmin(cost, rec(i-k, K) + abs(H[i] - H[i-k]));
        }
    }

    return dp[i]=cost;
}

int main() {
    int N, K; cin >> N >> K;
    dp.resize(N, LINF);
    H.resize(N, 0);
    REP(i, N) cin >> H[i];

    cout << rec(N-1, K) << endl;

    return 0;
}
