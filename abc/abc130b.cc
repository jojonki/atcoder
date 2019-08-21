#include <iostream>
using namespace std;

int main() { 
    int N, X;
    cin >> N >> X;
    int L[N];
    int i = 0;
    for (int i=0; i<N; i++) {
        cin >> L[i];
    }

    int ct = 1;
    int dist = 0;
    for (int i=0; i<N; i++) {
        if (dist + L[i] <= X) {
            ct++;
        } else {
            break;
        }
        dist += L[i];
    }

    cout << ct << endl;
    
    return 0;
}