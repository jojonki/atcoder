#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;

ll N;
vector<ll> H;

int main() { 
    cin >> N;
    H.resize(N);
    ll ct = 0;
    ll tmpct = 0;
    cin >> H[0];
    for(int i=1; i<N; i++) {
        cin >> H[i];
        if(H[i-1] >= H[i]) {
            tmpct++;
        } else {
            ct = max(tmpct, ct);
            tmpct =0;
        }
    }
    cout << max(ct, tmpct) << endl;

    
    return 0;
}