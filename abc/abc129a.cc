#include <iostream>
using namespace std;

int main() { 
    int P, Q, R;
    cin >> P >> Q >> R;

    cout << min(min(P+Q, Q+R), P+R) << endl;
    
    return 0;
}