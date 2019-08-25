#include <iostream>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const ll INF = 1e9;

int W[101];
int V[101];
ll dp[101][1000001] = {0};
ll sumW[101][1000001] = {0};

int main() {
    int N, limW; cin >> N >> limW;

    REP(i, N) {
        cin >> W[i] >> V[i];
    }

    REP(i, N) {
        REP(sumW, limW+1) {
            ll score = dp[i][sumW];
            if (sumW >= W[i]) { // pickup this item
                chmax(score, dp[i][sumW-W[i]] + V[i]);
            }
            dp[i+1][sumW] = score;
        }
    }

    // REP(i, N+1) {
    //     REP(w, limW+1) {
    //         cout << dp[i][w] << " ";
    //     }
    //     cout << endl;
    // }
    cout << dp[N][limW] << endl;

    return 0;
}