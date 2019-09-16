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


typedef pair<int, int> p;
int main() { 
    int x1, y1; cin >> x1 >> y1;
    int x2, y2; cin >> x2 >> y2;
    int x3, y3, x4, y4;

    int dx = x2 - x1;
    int dy = y2 - y1;

    x3 = x2 - dy;
    y3 = y2 + dx;
    x4 = x1 - dy;
    y4 = y1 + dx;
    
    print(x3, y3, x4, y4);
    
    return 0;
}