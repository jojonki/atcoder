#include <iostream>
#include <vector>
#include <iomanip>
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
    int N; cin >> N;
    vector<int> P;
    REP(i, N) {
        int p; cin >> p;
        P.push_back(p);
    }

    int maxV = *max_element(P.begin(), P.end());
    bool useHangaku = false;
    int price = 0;
    REP(i, N) {
        if (P[i] == maxV && !useHangaku) {
            price += P[i]/2;
            useHangaku = true;
        } else {
            price += P[i];
        }
    }

    cout << price << endl;
    
    return 0;
}