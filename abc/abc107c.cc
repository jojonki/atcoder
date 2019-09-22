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


int main() { 
    int N, K; cin >> N >> K;
    vector<ll> X(N, 0);
    REP(i, N) {
        cin >> X[i];
    }
    ll cost = LINF;
    REP(i, N-K+1) {
        ll tmpC = 0;
        ll left = X[i];
        ll right = X[i+K-1];
        if(left*right >= 0) { // same direction
            tmpC = (ll)(max(abs(left), abs(right)));
        } else { // different direction
            if(abs(left) < abs(right)) {
                tmpC = (ll)(2 * abs(left) + abs(right));
            } else {
                tmpC = (ll)(2 * abs(right) + abs(left));
            }
        }
        chmin(cost, tmpC);
    }

    print(cost);
    
    return 0;
}