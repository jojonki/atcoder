#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <bitset>
using namespace std;
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
inline void print() { cout << endl; }
template <class Head, class... Tail> inline void print(Head&& head, Tail&&... tail) {cout << head; if (sizeof...(tail) != 0) cout << " "; print(forward<Tail>(tail)...);}
template <class T> inline void print(vector<T>& vec) { for (auto& a : vec) {cout << a; if (&a != &vec.back()) cout << " "; } cout << endl;}
template <class T> inline void print(vector<vector<T>>& df) { for (auto& vec : df) { print(vec); }}
const unsigned int BIT_0 = (1 << 0); // 0000 0000 0000 0001
const unsigned int BIT_1 = (1 << 1); // 0000 0000 0000 0010
const unsigned int BIT_2 = (1 << 2); // 0000 0000 0000 0100
const unsigned int BIT_3 = (1 << 3); // 0000 0000 0000 1000
const unsigned int BIT_4 = (1 << 4); // 0000 0000 0001 0000
const unsigned int BIT_5 = (1 << 5); // 0000 0000 0010 0000
const unsigned int BIT_6 = (1 << 6); // 0000 0000 0100 0000
const unsigned int BIT_7 = (1 << 7); // 0000 0000 1000 0000

typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;

bool myComparison(const pair<ll,ll> &a,const pair<ll,ll> &b)
{
       return a.second>=b.second;
}

int main() { 
    int N, M; cin >> N >> M;
    vector<ll> A(N);
    REP(i, N) {
        ll a; cin >> a;
        A[i] = a;
    }

    vector<pair<ll, ll>> big; // (A.idx, val)
    int maxBit = 63;
    REP(s, maxBit) {
        int shift = maxBit-s;
        REP(i, N) {
            if(A[i] & (1 << shift)) {
                // print("shift", shift);
                // big.push_back(make_pair(i, A[i]));
                big.push_back(make_pair(A[i], i));
            }
        }
        // print(A);


        if(big.size() > 0) {
            // print("----");
            // sort(big.begin(), big.end(), myComparison);//greater<pair<int, int>>());
            sort(big.begin(), big.end(), greater<pair<int, int>>());
            // REP(i, big.size()) {
            //     print("====", big[i].first, big[i].second);
            // }

            REP(i, big.size()) {
                // print("i=", i, "big v=", big[i].second, "A idx=", big[i].first);
                // A[big[i].first] = A[big[i].first] >> 1;
                A[big[i].second] = A[big[i].second] >> 1;
                // print("new A[big[i].first]=", A[big[i].first]);
                // print(A);
                M--;
                // print("M=", M);
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