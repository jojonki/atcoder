#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
using namespace std;

int main()
{
    int N;
    vector<int> dv;
    cin >> N;
    while(N--) {
        int d;
        cin >> d; 

        vector<int>::iterator it = find(dv.begin(), dv.end(), d);
        if(it == dv.end()) {
            dv.push_back(d);
        }
    }

    cout << dv.size() << endl;
    return 0;
}