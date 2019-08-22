#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() { 
    int N;
    cin >> N;
    vector<int> V;
    int tmp = N;
    while(tmp--) {
        int v;
        cin >> v;
        V.push_back(v);
    }
    
    sort(V.begin(), V.end());

    double val = (double)(V[0] + V[1]) / 2.0;
    for (int i=2; i<N; i++) {
        val = (val + V[i]) / 2.0;
    }

    cout << val << endl;
    
    return 0;
}