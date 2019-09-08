#include <iostream>
#include <vector>
#include <iomanip>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;

int main() {
    int N, M; cin >> N >> M;
    vector<int> X;
    vector<int> df;
    REP(i, M) {
        int x; cin >> x;
        X.push_back(x);
    }

    sort(X.begin(), X.end());

    REP(i, X.size()-1) {
        df.push_back(X[i+1]-X[i]);
    }
    sort(df.begin(), df.end());

    ll ct = 0;
    int sumup_ct = (M-1) - (N-1);
    if(sumup_ct > 0) {
        REP(i, sumup_ct) {
            ct += df[i];
        }
    }
    cout << ct << endl;
    
    return 0;
}