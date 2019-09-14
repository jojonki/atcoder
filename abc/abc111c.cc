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

typedef tuple<int, int, int> tri;

vector<int> get_unique(vector<int> v) {
    // sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    return v;
}

tri counter(const vector<int> &org, const vector<int> &uv) {
    int max_ct1 = 0;
    int max_ct2 = 0;
    int max_v = -1;
    int last_lb = 0;
    int ct = 0;
    REP(i, uv.size()) {
        int lb = upper_bound(org.begin(), org.end(), uv[i]) - org.begin();
        ct = lb - last_lb;
        last_lb = lb;
        if (ct > max_ct1) {
            max_ct2 = max_ct1;
            max_ct1 = ct;
            max_v = uv[i];
        } else if(ct > max_ct2) {
            max_ct2 = ct;
        }
    }

    return make_tuple(max_v, max_ct1, max_ct2);
}

int main() { 
    int n; cin >> n;
    vector<int> v1(n/2);
    vector<int> v2(n/2);
    REP(i, n) {
        if(i%2==0) cin >> v1[i/2];
        else cin >> v2[i/2];
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    auto uv1 = get_unique(v1);
    auto uv2 = get_unique(v2);
    int res = 0;
    auto tri1= counter(v1, uv1);
    int maxv1 = get<0>(tri1);
    int ct11 = get<1>(tri1);
    int ct12 = get<2>(tri1);

    auto tri2= counter(v2, uv2);
    int maxv2 = get<0>(tri2);
    int ct21 = get<1>(tri2);
    int ct22 = get<2>(tri2);

    if (maxv1 == maxv2) {
        if(ct12>ct22) {
            res += (n/2) - ct12;
            res += (n/2) - ct21;
        } else {
            res += (n/2) - ct11;
            res += (n/2) - ct22;
        }
    } else {
        res += (n/2) - ct11;
        res += (n/2) - ct21;
    }

    print(res);
    
    return 0;
}