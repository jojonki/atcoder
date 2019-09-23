#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <algorithm>
using namespace std;
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
inline void print() { cout << endl; }
template <class Head, class... Tail> inline void print(Head&& head, Tail&&... tail) {cout << head; if (sizeof...(tail) != 0) cout << " "; print(forward<Tail>(tail)...);}
template <class T> inline void print(vector<T>& vec) { for (auto& a : vec) {cout << a; if (&a != &vec.back()) cout << " "; } cout << endl;}
template <class T> inline void print(vector<vector<T>>& df) { for (auto& vec : df) { print(vec); }}
typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;

long double mlog(ll base, ll val) {
    if(val==0) return 0;
    return logl(val) / log(base);
}

int main() { 
    string S; cin >> S;
    ll K; cin >> K;
    ll T = 5e15;
    ll ct = 0;
    REP(i, S.size()) {
        ll base = S[i]-'0';
        if(base == 1) {
            ct += 1;
        } else if(mlog(base, ct) + T >= mlog(base, K)) {
            print(base);
            return 0;
        } else {
            ct += powl(base, T);
        }

        if(ct == K) {
            print(base);
            return 0;
        }
    }
    print(S[0]-'0');
    
    return 0;
}