#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
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
    int s; cin >> s;
    vector<int> v;
    int a = s;
    v.push_back(a);
    REP(i, 1000001) {
        if (a%2==0) {
            a = a/2;
        } else {
            a = 3*a + 1;
        }
        if (find(v.begin(), v.end(), a) != v.end()) {
            cout << i+2 << endl;
            break;
        }
        v.push_back(a);
    }
    
    return 0;
}