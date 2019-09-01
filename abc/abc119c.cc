#include <iostream>
#include <algorithm>
#include <vector>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
const int INF = 1e9;
using namespace std;

int A, B, C, N;
vector<int> L;

int rec(int i, int a, int b, int c) {
    // 竹L[i]を，cond 1-4に分けて再帰的に探索
    if (i==N) {
        if(!a || !b || !c) return INF;
        return abs(a-A) + abs(b-B) + abs(c-C);
    }

    // cond 1: 今ある竹を利用しない
    int res = rec(i+1, a, b, c);

    // cond 2-4: A, B, Cを使う場合
    chmin(res, rec(i+1, a+L[i], b, c) + (a?10:0));
    chmin(res, rec(i+1, a, b+L[i], c) + (b?10:0));
    chmin(res, rec(i+1, a, b, c+L[i]) + (c?10:0));


    return res;
}

int main() {
    cin >> N >> A >> B >> C;
    L.resize(N);
    REP(i, N) cin >> L[i];

    cout << rec(0, 0, 0, 0) << endl;

    return 0;
}