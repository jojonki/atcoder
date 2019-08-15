#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> H;
    while(N--) {
        int h;
        cin >> h;
        H.push_back(h);
    }

    bool valid = true;
    for (int i=H.size()-1; i>0; i--) {
        int ldiff = H[i] - H[i-1];
        if (ldiff == -1) {
            H[i-1]--;
        } else if (ldiff < -1) {
            valid = false;
            break;
        }
    }

    if(valid) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}