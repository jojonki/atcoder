#include <iostream>
using namespace std;

int main() { 
    int A, B, T;
    cin >> A >> B >> T;

    int ct = 0;
    int t = A;
    float limit = (float)T + 0.5;

    while(true) {
        if (t > limit) break;

        ct += B;
        t += A;
    }

    cout << ct << endl;
    
    return 0;
}