#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() { 
    int N, Q; cin >> N >> Q;
    string S; cin >> S;
    auto cter = vector<int>(N, 0);
    int ct = 0;
    for (int i=1; i<N; i++) {
        if (S[i-1] == 'A' && S[i]=='C') ct++;
        cter[i] = ct;
    }

    for (int i=0; i<Q; i++) {
        int l, r; cin >> l >> r;
        l--; r--;
        cout << cter[r] - cter[l] << endl;
    }
    
    return 0;
}