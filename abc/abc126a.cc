#include <iostream>
#include <algorithm>
using namespace std;

int main() { 
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    for (int i=0; i<N; i++) {
        if (i==K-1) {
            cout << tolower(S[i], locale());
        } else {
            cout << S[i];
        }
    }
    cout << endl;
    
    return 0;
}