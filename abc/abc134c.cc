
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
    int N;
    int maxV[] = {0, 0};
    int maxCt[] = {0, 0};
    vector<int> A;
    cin >> N;
    for (int i=1; i<N+1; i++) {
        int a;
        cin >> a;
        if (a == maxV[0]) {
            maxCt[0]++;
        } else if (a == maxV[1]) {
            maxCt[1]++;
        } else if (a > maxV[0]) {
            maxV[1] = maxV[0];
            maxCt[1] = maxCt[0];

            maxV[0] = a;
            maxCt[0] = 1;
        } else if (a > maxV[1]) {
            maxV[1] = a;
            maxCt[1] = 1;
        }
        A.push_back(a);
    }

    for (int i=0; i<N; i++) {
        if (A[i] == maxV[0]) {
            if (maxCt[0] > 1) {
                cout << maxV[0] << endl;
            } else {
                cout << maxV[1] << endl;
            }
        } else {
            cout << maxV[0] << endl;
        }
    }

    return 0;
}