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
int main() { 
    cin >> N;

    ll ct = 0;
    if (N>1) {
        REP(i, N-1) ct += (i+1);
    }
    cout << ct << endl;

    
    return 0;
}