#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n, d;
    cin >> n >> d;
    
    cout << (int)(ceil(1.0 * n / (2*d+1))) << endl;

    return 0;
}