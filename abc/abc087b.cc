#include<iostream>
using namespace std;

int main()
{
    int A, B, C, X, count = 0;
    cin >> A >> B >> C >> X;

    int Xt = X / 50;
    int At[A+1], Bt[B+1], Ct[C+1];
    for (int i=0; i<A+1; i++) {
        At[i] = i * (500/50);
    }
    for (int i=0; i<B+1; i++) {
        Bt[i] = i * (100/50);
    }
    for (int i=0; i<C+1; i++) {
        Ct[i] = i * (50/50);
    }

    for (int i=0; i<A+1; i++) {
        for (int j=0; j<B+1; j++) {
            for (int k=0; k<C+1; k++) {
                if ((At[i]+ Bt[j] + Ct[k]) == Xt) count++;
            }
        }
    }

    cout << count << endl;

    return 0;
}