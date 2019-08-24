#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

bool sortbysec(const pair<int, int> &a, const pair<int, int> &b) {
    return a.first < b.first;
}

int main() { 
    int N, M; cin >> N >> M;
    vector<pair<ll, ll>> D;

    for (int i=0; i<N; i++) {
        ll a, b; cin >> a >> b;
        D.push_back(make_pair(a, b));
    }
    sort(D.begin(), D.end(), sortbysec);

    ll cost = 0;
    int ct = 0;
    for (auto v: D) {
        ll rest = M - ct;
        ll buy = min(rest, v.second);
        cost += buy * v.first;
        ct += buy;
    }
    cout << cost << endl;
    
    return 0;
}