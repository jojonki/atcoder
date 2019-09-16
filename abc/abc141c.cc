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
    int N, K, Q; cin >> N >> K >> Q;
    // print(K, Q);
    vector<int> A(N);
    vector<int> P(N);
    REP(i, N) {P[i] = K-Q;}

    // print(P);
    REP(i, Q) {
        int a; cin >> a;
        // cin >> A[i];
        // print("====A[i]", A[i]);
        // print("before", P[A[i-1]]);
        P[a-1] += 1;
        // print("after", P[A[i-1]]);
    }
    // print(A);
    // print(P);

    REP(i, N) {
        // print("i+1=", i+1, "P[i]=", P[i]);
        if(P[i]>0) {
            print("Yes");
        } else {
            print("No");
        }
    }
    
    return 0;
}