#include <iostream>
#include <vector>
#include <numeric>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;

int main() {
    int N; cin >> N;
    vector<int> L;
    REP(i, N) {
        int l; cin >> l;
        L.push_back(l);
    }
    sort(L.begin(), L.end());

    if(accumulate(L.begin(), L.end()-1, 0) > L[L.size()-1]) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    
    return 0;
}