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

template <typename T1, typename T2>
bool compare_by_second(const pair<T1, T2> &a, const pair<T1, T2> &b) {
    if (a.second != b.second) {
        return a.second < b.second;
    } else {
        return a.first < b.first;
    }
}
void show(const vector<pair<int, int>> &v) {
    // print("______");
    // print(v.size());
    REP(i, v.size()) {
        // print(v[i].second);
        cout << v[i].second << " ";
    }
    cout << endl;
}


int main() { 
    int N; cin >> N;
    vector<pair<int, int>> A;
    REP(i, N) {
        int a; cin >> a;
        auto p = make_pair(a, i+1);
        // print(p.first, p.second);
        A.push_back(p);
    }
    sort(A.begin(), A.end());
    // sort(A.begin(), A.end(), greater<pair<int, int>>());
    show(A);

    
    return 0;
}