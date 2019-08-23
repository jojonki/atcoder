#include <iostream>
using namespace std;

int main() { 
    int a,b,c,d,e,k;
    int at[5];
    for(int i=0; i<5; i++) {
        int p; cin >> p;
        at[i] = p;
    }
    cin >> k;
    bool ok = true;
    for (int i=0; i<4; i++) {
        for (int j=i; j<5; j++) {
            if (at[j] - at[i] > k) {
                ok = false;
                break;
            }

        }
    }

    if(ok) cout << "Yay!" << endl;
    else cout << ":(" << endl;
    
    return 0;
}