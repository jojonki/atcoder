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

vector<int> H;

int main() {
    int N; cin >> N;
    vector<int> h(N);
    int maxH = 0;
    REP(i, N) {
        cin >> h[i]; chmax(maxH, h[i]);
    }
    vector<vector<int>> m(maxH, vector<int>(N));
    REP(height, maxH) {
        REP(i, N) {
            if (h[i] >= height+1) {
                m[height][i] = 1;
            } else {
                m[height][i] = 0;
            }
        }
    }
    int ct = 0;
    REP(height, maxH) {
        bool reset = true;
        REP(i, N) {
            if (reset && m[height][i] == 1) {
                ct++;
                reset = false;
            } else if(m[height][i] == 0 && !reset) {
                reset = true;
            }
        }
    }
    // print(m);
    cout << ct << endl;
    
    return 0;
}
