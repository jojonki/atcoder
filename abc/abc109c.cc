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

int gcd(int A, int B) {
    int rem;
    if(A<B) {
        int tmp = A;
        A = B;
        B = tmp;
    }
    rem = A % B;
    if (rem == 0) {
        return B;
    }

    return gcd(B, rem);
}

int main() { 
    int N, X; cin >> N >> X;
    vector<int> P(N);
    vector<int> dist(N);
    int x;
    cin >> x;
    dist[0] = abs(X-x);
    int divisor = dist[0];
    REP(i, N-1) {
        cin >> x;
        dist[i] = abs(X-x);
        divisor = gcd(divisor, dist[i]);
    }
    // print(dist);

    print(divisor);
    
    return 0;
}