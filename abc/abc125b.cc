#include <iostream>
#include <vector>
using namespace std;

int main() { 
    int N; cin >> N;
    vector<int> V;
    for (int i=0; i<N; i++) {
        int v; cin >> v;
        V.push_back(v);
    }
    int maxP = 0;
    for (int i=0; i<N; i++) {
        int c; cin >> c;
        if (V[i]-c>0) maxP += (V[i]-c);
    }

    cout << maxP << endl;
    
    return 0;
}