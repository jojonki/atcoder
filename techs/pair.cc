
#include <iostream>
#include <vector>
#include <random>
using namespace std;
#define REP(i, n) for(int i = 0; i < n; i++)
inline void print() { cout << endl; }
template <class Head, class... Tail> inline void print(Head&& head, Tail&&... tail) {cout << head; if (sizeof...(tail) != 0) cout << " "; print(forward<Tail>(tail)...);}
template <class T> inline void print(vector<T>& vec) { for (auto& a : vec) {cout << a; if (&a != &vec.back()) cout << " "; } cout << endl;}
template <class T> inline void print(vector<vector<T>>& df) { for (auto& vec : df) { print(vec); }}

template <typename T1, typename T2>
bool compare_by_second(const pair<T1, T2> &a, const pair<T1, T2> &b) {
    if (a.second != b.second) {
        return a.second < b.second;
    } else {
        return a.first < b.first;
    }
}

void show(const vector<pair<int, int>> &v) {
    print("______");
    REP(i, v.size()) {
        print(v[i].first, v[i].second);
    }
}

int main() {
    vector<pair<int, int>> pt;
    random_device rnd;
    pt.push_back(make_pair(3, 10));
    pt.push_back(make_pair(3, 21));
    pt.push_back(make_pair(3, 1));
    pt.push_back(make_pair(3, 8));
    pt.push_back(make_pair(5, 1));
    pt.push_back(make_pair(15, 1));
    pt.push_back(make_pair(7, 1));
    pt.push_back(make_pair(78, 1));
    REP(i, 4) {
        pt.push_back(make_pair(rnd()%100, rnd()%20));
        // pt.push_back(make_pair(i, rnd()%20));
    }

    show(pt);

    sort(pt.begin(), pt.end());
    sort(pt.begin(), pt.end(), greater<pair<int, int>>());
    show(pt);

    sort(pt.begin(), pt.end(), compare_by_second<int, int>);
    show(pt);

    return 0;
}