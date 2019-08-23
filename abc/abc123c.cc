#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;
typedef long long ll;
int main() { 
    ll N; cin >> N;
    ll bn = pow(10, 15);
    for(int i=0; i<5; i++) {
        ll c; cin >> c;
        bn = min(bn, c);
    }
    cout << setprecision(16) << ceil(double(N)/bn)+4 << endl;
    
    return 0;
}