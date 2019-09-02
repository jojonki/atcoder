#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;

int main() { 
    int A, B; cin >> A >> B;

    if(B==1) {
        cout << 0 << endl;
        return 0;

    }


    int C = B-A;
    if (C <= 0) {
        cout << 1 << endl;
    } else {
        cout << (int)(ceil(1.0*C/(A-1))) + 1 << endl;
    }


    
    return 0;
}