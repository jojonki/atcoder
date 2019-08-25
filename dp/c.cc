#include <iostream>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;

const int K = 3; // a, b, c
ll dp[100001][K];
ll a[100001][K];

int main() {
    int N; cin >> N;
    REP(i, N) cin >> a[i][0] >> a[i][1] >> a[i][2];

    for(int i=0; i<N; i++) {
        REP(k1, K) { // i+1
            ll score = 0;
            REP(k2, K) { // i
                if (k1 != k2) {
                    chmax(score, dp[i][k2]+a[i][k2]);
                }
            }
            dp[i+1][k1] = score;
        }
    }

    cout << max({dp[N][0], dp[N][1], dp[N][2]}) << endl;

    return 0;
}