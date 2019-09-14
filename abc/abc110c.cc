#include <iostream>
#include <map>
#include <iomanip>
#include <cmath>
#include <algorithm>
using namespace std;
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;


int main() { 
    string S, T; cin >> S >> T;
    map<char, char> st;
    map<char, char> ts;

    REP(i, S.size()) {
        char x = S[i];
        char y = T[i];
        if (st.count(x) == 0) {
            st[x] = y;
        } else {
            if (st[x] != y) {
                cout << "No" << endl;
                return 0;
            }
        }
        if (ts.count(y) == 0) {
            ts[y] = x;
        } else {
            if (ts[y] != x) {
                cout << "No" << endl;
                return 0;
            }
        }
    }

    cout << "Yes" << endl;

    return 0;
}