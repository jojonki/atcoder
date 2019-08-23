#include <iostream>
using namespace std;

const int C=20;
typedef long long ll;
int main() { 
    string S; cin >> S;
    ll N = S.size();

    ll ct1=0;
    ll ct2=0;
    for (int i=0; i<N; i++) {
        bool cl = (S[i] == '1');
        if (i%2==0) {
            if (!cl) ct1++;
            if (cl) ct2++;
        } else {
            if (cl) ct1++;
            if (!cl) ct2++;
        }
    }
    cout << min(ct1, ct2) << endl;
    
    return 0;
}