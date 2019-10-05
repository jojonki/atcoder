#include<iostream>
using namespace std;

typedef long long ll;

ll gcd(ll A, ll B) {
    return B? gcd(B, A%B) : A;
}


int main() {
    cout << gcd(18, 12) << endl;
    cout << gcd(12, 18) << endl;

    return 0;
}