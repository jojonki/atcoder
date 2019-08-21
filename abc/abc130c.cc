#include <iostream>
#include <iomanip>
using namespace std;

int main() { 
    int W, H, x, y;
    cin >> W >> H >> x >> y;

    double s = (double)(W) * H / 2;
    cout << fixed << setprecision(10) << s << endl;

    double x2 = x * 2.0;
    double y2 = y * 2.0;

    if (x2 == W && y2 == H) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
    
    return 0;
}