#include <iostream>
using namespace std;

int main()
{
    int k, x;
    cin >> k >> x;

    int maxX = 1000000;
    int candBeg = max(x - (k-1), maxX * (-1));
    int candEnd = min(x + (k-1), maxX);

    for (int i=candBeg; i<=candEnd; i++) {
        cout << i;
        if (i!=candEnd) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}