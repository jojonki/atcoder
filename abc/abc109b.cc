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
    int N; cin >> N;
    vector<string> W;
    string s; cin >> s;
    W.push_back(s);
    REP(i, N-1) {
        string next_s; cin >> next_s;
        if(find(W.begin(), W.end(), next_s) != W.end()) {
            print("No");
            return 0;
        }
        if(next_s[0] != s[s.size()-1]) {
            print("No");
            return 0;
        }
        W.push_back(next_s);
        s = next_s;
    }
        
    print("Yes");
    
    return 0;
}