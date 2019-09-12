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
    int N, M; cin >> N >> M;
    vector<vector<int>> vals(N);
    vector<int> P, Y;
    REP(i, M) {
        int p, y; cin >> p >> y; --p;
        P.push_back(p); Y.push_back(y);
        vals[p].push_back(y);
    }

    REP(i, N) {
        sort(vals[i].begin(), vals[i].end());
    }

    REP(i, M) {
        int p = P[i];
        printf("%06d", p+1);
        int id = lower_bound(vals[p].begin(), vals[p].end(), Y[i]) - vals[p].begin();
        printf("%06d\n", id+1);
    }


    // print(table);

    return 0;
}