#include <iostream>
#include <vector>
using namespace std;

int main() {
    string S;
    cin >> S;

    bool good = true;
    for (int i=0; i<S.size()-1; i++) {
        if (S.at(i) == S.at(i+1)) {
            good = false;
            break;
        }
    }

    if (good) {
        cout << "Good" << endl;
    } else {
        cout << "Bad" << endl;
    }

    return 0;
}