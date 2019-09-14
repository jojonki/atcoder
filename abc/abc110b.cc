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
    int N, M, X, Y; cin >> N >> M >> X >> Y;
    vector<int> x(N), y(M);
    REP(i, N) {
        cin >> x[i];
    }
    REP(i, M) {
        cin >> y[i];
    }
    sort(x.begin(), x.end());
    sort(y.begin(), y.end());
    int maxX = x[N-1];
    int minY = y[0];

    if(X >= Y) {
        print("War");
        return 0;
    }
    vector<int> Z;
    for(int i=X+1; i<=Y; i++) {
        Z.push_back(i);
    }

    bool found = false;
    REP(i, Z.size()) {
        int z = Z[i];
        if (maxX < z && z <= minY) {
            found = true;
            break;
        }
    }

    if(found) {
        print("No War");
    } else {
        print("War");
    }

    return 0;
}