#include <iostream>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const ll INF = 1e9;

const int MAX_N = 101;
const int MAX_V = 100001;
int W[MAX_N];
int V[MAX_N];
ll dp[MAX_N][MAX_V]={0};
ll sumV[MAX_N][MAX_V] = {0};

int main() {
    int N, limW; cin >> N >> limW;

    REP(i, MAX_N) {
        cin >> W[i] >> V[i];
        REP(v, MAX_V) dp[i][v] = LINF;
    }
    dp[0][0] = 0;

    REP(i, N) {
        REP(sumV, MAX_V) {
            if(sumV >= V[i]) {
                chmin(dp[i+1][sumV], dp[i][sumV-V[i]] + W[i]);
            }
            chmin(dp[i+1][sumV], dp[i][sumV]);
        }
    }

    int res=0;
    REP(v, MAX_V) {
        if(dp[N][v] <= limW) res=v;
    }
    cout << res << endl;

    return 0;
}