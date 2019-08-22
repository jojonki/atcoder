#include <iostream>
#include <vector>
using namespace std;

int main() { 
    int N, M;
    cin >> N >> M;
    int maxL = 0;
    int minR = N;
    for (int i=0; i<M; i++) {
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        if (l > maxL) maxL = l;
        if (r < minR) minR = r;
    }

    int res = max(0, minR - maxL + 1);

    cout << res << endl;
    
    return 0;
}