#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    vector<int> P;
    cin >> N;
    while(N--) {
        int p;
        cin >> p;
        P.push_back(p);
    }

    int ct = 0;
    for (int i=1; i<P.size()-1; i++) {
        if (P[i-1] < P[i]) {
            if (P[i] < P[i+1]) ct++;
        } else {
            if (P[i] > P[i+1]) ct++;
        }
    }
    cout << ct << endl;

    return 0;
}