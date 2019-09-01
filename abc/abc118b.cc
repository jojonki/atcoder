#include <iostream>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const ll INF = 1e9;


int L[30] = {0};
int main() { 
    int N, M;
    cin >> N >> M;

    REP(i, N) {
        int K; cin >> K;
        REP(j, K) {
            int a; cin >> a;
            L[a-1]++;
        }
    }

    int ct = 0;
    REP(i, M) {
        if(L[i] == N) ct++;
    }
    cout << ct << endl;
    
    
    return 0;
}