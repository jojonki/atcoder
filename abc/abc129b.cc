#include <iostream>
using namespace std;

int main() { 
    int N;
    cin >> N;
    int W[N];
    for (int i=0; i<N; i++) {
        cin >> W[i];
    }

    int mins = 10000;
    for (int T=0; T < N-1; T++) {
        int s1 = 0;
        int s2 = 0;
        for (int i=0; i<=T; i++) {
            s1 += W[i];
        }
        for (int i=T+1; i<N; i++) {
            s2 += W[i];
        }

        mins = min(mins, abs(s1-s2));
    }

    cout << mins << endl;
   
    return 0;
}