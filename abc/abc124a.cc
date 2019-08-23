#include <iostream>
using namespace std;

int main() { 
    int A, B;
    cin >> A >> B;

    int sum = 0;
    for (int i=0; i<2; i++) {
        if (A>B) {
            sum += A;
            A--;
        } else {
            sum += B;
            B--;
        }
    }

    cout << sum << endl;
    
    return 0;
}