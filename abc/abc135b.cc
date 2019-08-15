#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> P1, P2;
    while(N--) {
        int p;
        cin >> p;
        P1.push_back(p);
        P2.push_back(p);
    }

    sort(P2.begin(), P2.end());

    bool valid = true;
    int dct = 0;
    for (int i=0; i<P1.size(); i++) {
        if (P1[i] != P2[i]) {
            dct++;
            if (dct > 2) {
                valid = false;
            }
        }
    }

    if (valid) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }


    return 0;
}