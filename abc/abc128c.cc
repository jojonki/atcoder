#include <iostream>
#include <bitset>
#include <vector>
using namespace std;

int main() { 
    int N, M;
    cin >> N >> M;
    vector<vector<int>> S(M);
    vector<int> P;
    for (int i=0; i<M; i++) {
        int k; cin >> k;

        for (int j=0; j<k; j++) {
            int s; cin >> s;
            S[i].push_back(s-1);
        }
    }
    for (int i=0; i<M; i++) {
        int p; cin >> p;
        P.push_back(p);
    }

    long long res = 0;
    for (int bit=0; bit<(1<<N); bit++) { // スイッチ全パターン
        bool on = true;
        // cout << bitset<8>(bit) << endl;
        for (int i=0; i<M; i++) { // 各電球が付いているかチェック
            int con = 0;
            for (auto v: S[i]) { // 接続スイッチ数のカウント
                if (bit & (1<<v)) con++;
            }
            if (con % 2 != P[i]) {
                on = false;
                break;
            }
        }
        if (on) res++;
    }

    cout << res << endl;
    
    return 0;
}