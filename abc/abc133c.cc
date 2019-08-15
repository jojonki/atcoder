#include <iostream>
#include <cmath>
using namespace std;
typedef long long ll;

int main()
{
    ll L, R;
    cin >> L >> R;
    
    ll md = 2018;
    if (R-L > 2019) {
        md = 0;
    } else {
        for(ll l=L; l<R; l++) {
            for(ll r=l+1; r<=R; r++) {
                ll lr_mod = (l*r) % 2019;
                md = min(md, lr_mod);
                if (md == 0) {
                    break;
                }
            }
        }
    }

    cout << md << endl;
    
    return 0;
}