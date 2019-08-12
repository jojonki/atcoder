#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int t[N];
    int x[N];
    int y[N];
    int i = 0;
    while (i<N) {
        cin >> t[i] >> x[i] >> y[i];
        i++;
    }

    bool impossible = false;
    for (int i=0; i<N; i++) {
        int tDiff = t[i];
        int xDiff = x[i];
        int yDiff = y[i];
        int xyDiff = xDiff + yDiff;
        if ((xyDiff > tDiff) ||  (tDiff + xyDiff) % 2 != 0) {
            impossible = true;
            break;
        }
    }
    if (impossible) { 
        cout << "No" << endl;
    } else {
        cout << "Yes" << endl;
    }

    return 0;
}
