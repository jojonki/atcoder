#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;

    int ct = 0;
    for (int i=1; i<=N; i++) {
        string s = to_string(i);
        if (s.size() % 2 == 1) ct++;
    }

    cout << ct << endl;

    return 0;
}