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

ll gcd(ll x, ll y) {
    return y? gcd(y, x%y) : x;
}

vector<pair<ll, int>> factorize(ll n) {
    vector<pair<ll, int>> res;
    res.emplace_back(1, 1);
    for(ll i=2; i*i<=n; i++) {
        if(n%i) continue;
        res.emplace_back(i, 0);
        while(n%i == 0) {
            res.back().second++;
            n /= i;
        }
    }
    if(n>1) {
        res.emplace_back(n, 1);
    }

    return res;
}

void print_factorize(vector<pair<ll, int>> f) {
    for(auto a: f) {
        cout << a.first << "^" << a.second << endl;;
    }
}

int main() {
    ll A, B; cin >> A >> B;
    ll g = gcd(A, B);
    // print("g=", g);
    auto f = factorize(g);
    // print_factorize(f);
    print(f.size());

}