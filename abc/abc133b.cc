#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
    int N, D;
    cin >> N >> D;

    vector<vector<int> > X(N, vector<int>(D));
    for (int i=0; i<N; i++) {
        for (int d=0; d<D; d++) {
            int x;
            cin >> X.at(i).at(d);
        }
    }

    int ct=0;
    for (int i=0; i<N-1; i++) {
        for (int j=i+1; j<N; j++) {
            int s = 0;
            for (int d=0; d<D; d++) {
                s += pow((X.at(i).at(d) - X.at(j).at(d)), 2);
            }
            for (int p=0; p<127; p++) {
                if (s == pow(p, 2)) {
                    ct++;
                    break;
                }
            }
        }
    }

    cout << ct << endl;
    
    return 0;
}