#include <iostream>
using namespace std;
typedef long long ll;

int main() {
    ll A, B, C, D;
    cin >> A >> B >> C >> D;

    ll nc, nd, nl;
    nc = (B - B/C) - ((A-1) - (A-1) / C);
    nd = (B - B/D) - ((A-1) - (A-1) / D);

    ll quot, rem; 
    int d = D;
    int c = C;
    ll G, L;
    while(true) {
        quot = d / c; 
        rem = d % c;
        if (rem == 0) {
            G = c;
            L = C * D / G;
            break;
        }

        d = c;
        c = rem;
    }

    nl = (B - B/L) - ((A-1) - (A-1) / L);

    cout << (nc + nd - nl) << endl;
    
    return 0;
}