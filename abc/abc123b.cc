#include <iostream>
using namespace std;

int main() { 
    int M[5];
    int maxW = 0;
    int lastM = 0;
    for (int i=0; i<5; i++) {
        cin >> M[i];
        int mod = M[i]%10;
        if (mod != 0) {
            if (10-mod > maxW) {
                lastM = i;
                maxW = 10-mod;
            }
        }
    }

    int T = 0;
    for (int i=0; i<5; i++) {
        if (i==lastM || M[i] %10 == 0) {
            T += M[i];
        } else {
            T += 10 * (M[i] / 10) + 10;
        }
    }

    cout << T << endl;
    
    return 0;
}