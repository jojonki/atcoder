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
    string S; cin >> S;

    bool easy = true;
    REP(i, S.size()) {
        if ((i+1)%2==0) {
            if(S[i]=='R') {
                easy = false;
                break;
            }
        } else {
            if(S[i]=='L') {
                // print(i, "-===");
                easy = false;
                break;
            }

        }
    }

    if(easy) {
        print("Yes");
    } else {
        print("No");
    }
    
    return 0;
}