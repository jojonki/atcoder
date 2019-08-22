#include <iostream>
#include <iomanip>
using namespace std;

int main() { 
    int N;
    cin >> N;
    double deno = 0.0;
    for (int i=0; i<N; i++) {
        int a;
        cin >> a;
        deno += 1/(double)a;
    }

    cout << fixed << setprecision(5) << 1 / deno << endl;
    
    return 0;
}