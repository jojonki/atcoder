#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    vector<int> D;

    cin >> N;
    while(N--) {
        int n;
        cin >> n;
        D.push_back(n);
    }

    int ct = 0;
    if(D.size() % 2 == 0) {
        sort(D.begin(), D.end());
        int mid = D.size() / 2;
        for (int i=D[mid-1]+1; i<=D[mid]; i++) ct++;
    }

    cout << ct << endl;

    return 0;
}