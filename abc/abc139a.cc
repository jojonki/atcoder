#include <iostream>
#include <vector>
#include <iomanip>
#define REP(i, n) for(int i = 0; i < n; i++)
template<class T> inline void chmin(T& a, T b) {if (a>b) a=b; }
template<class T> inline void chmax(T& a, T b) {if (a<b) a=b; }
using namespace std;
typedef long long ll;
const ll LINF = 1e18;
const int INF = 1e9;

int main() { 
    string S, T;
    cin >> S >> T;
    int ct=0;
    REP(i, 3) {
        if (S[i]==T[i]) ct++;
    }
    cout << ct << endl;
    
    return 0;
}