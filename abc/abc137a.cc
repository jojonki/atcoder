#include <iostream>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    int max_r = max(max(a+b, a-b), a*b);

    cout << max_r << endl;

    return 0;
}