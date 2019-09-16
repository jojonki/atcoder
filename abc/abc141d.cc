#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <bitset>
#include <queue>
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
    priority_queue<int> products;
    REP(i, N) {
        int p; cin >> p;
        products.push(p);
    }
    REP(i, M) {
        int p = products.top();
        products.pop();
        products.push(p/2);
    }
    ll res = 0;
    while(!products.empty()) {
        res += products.top();
        products.pop();
    }

    print(res);

    return 0;
}

bool myComparison(const pair<ll,ll> &a,const pair<ll,ll> &b)
{
       return a.second>=b.second;
}

int main2() { 
    int N, M; cin >> N >> M;
    vector<ll> A(N);
    REP(i, N) {
        ll a; cin >> a;
        A[i] = a;
    }

    vector<pair<ll, ll>> big;
    int maxBit = 63;
    REP(s, maxBit) {
        int shift = maxBit-s;
        REP(i, N) {
            if(A[i] & (1 << shift)) {
                big.push_back(make_pair(A[i], i));
            }
        }

        if(big.size() > 0) {
            sort(big.begin(), big.end(), greater<pair<int, int>>());

            REP(i, big.size()) {
                A[big[i].second] = A[big[i].second] >> 1;
                M--;
                if(M<=0) {
                    break;
                }
            }
        }
        if(M<=0) {
            break;
        }
        big.clear();
    }

    ll res = 0;
    REP(i, N) {
        res += A[i];
    }
    cout << res << endl;;

    return 0;
}