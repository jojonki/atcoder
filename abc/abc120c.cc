#include <iostream>
using namespace std;

int main() { 
    string S; cin >> S;
    int N = S.length();
    int one = 0;
    int zero = 0;
    for (int i=0; i<N; i++) {
        if (S[i] == '1') one++;
        else if (S[i] == '0') zero++;
    }

    cout << min(one, zero) * 2 << endl;
    
    return 0;
}