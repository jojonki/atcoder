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



typedef pair<int, int> pt;

int dist(pt tgt, pt cent) {
    return abs(cent.first - tgt.first) + abs(cent.second - tgt.second);
}

int main() { 
    int N; cin >> N;
    vector<pt> P(N);
    vector<int> H;
    REP(i, N) {
        int x, y, h;
        cin >> x >> y >> h;
        P[i] = make_pair(x, y);
        H.push_back(h);
    }

    int cx, cy, ch;
    ch = 0;
    REP(x, 101) {
        REP(y, 101) {
            pt cent = make_pair(x, y); // candidate
            int start = 0;
            ll h = 0;
            REP(i, N) {
                if(H[i] > 0) {
                    h = dist(cent, P[i]) + H[i];
                    break;
                }
            }

            bool valid_pt = true;
            for(int i=0; i<N; i++) {
                int elm_h = h - dist(cent, P[i]);
                if (elm_h >= 0 && elm_h != H[i]) {
                    valid_pt = false;
                    break;
                } else if(elm_h<0 && H[i] != 0) {
                    valid_pt = false;
                    break;
                }
            }
            if (valid_pt) {
                if (h > ch) {
                    ch = h;
                    cx = x;
                    cy = y;
                }
            }
        }
    }
    print(cx, cy, ch);
    
    return 0;
}