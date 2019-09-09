#include <iostream>
#include <vector>
#include <cmath>
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

ll N;

void rec(ll cur, int use, ll& counter) {
    if (cur > N) return;

    if (use == 0b111) counter++;

    rec(cur * 10 + 7, use | 0b100, counter);
    rec(cur * 10 + 5, use | 0b010, counter);
    rec(cur * 10 + 3, use | 0b001, counter);
}

int main() { 
    cin >> N;
    ll res = 0;
    rec(0, 0, res);

    cout << res << endl;
    
    return 0;
}