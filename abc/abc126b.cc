#include <iostream>
using namespace std;

int main() { 
    string S; cin >> S;

    string pre_s{S[0], S[1]};
    string suf_s{S[2], S[3]};
    int pre = stoi(pre_s);
    int suf = stoi(suf_s);

    bool is_pre_mon = false;
    bool is_suf_mon = false;

    if (pre > 0 && pre < 13) {
        is_pre_mon = true;
    }
    if (suf > 0 && suf < 13) {
        is_suf_mon = true;
    }

    if (is_pre_mon && ! is_suf_mon) {
        cout << "MMYY" << endl;
    } else if (!is_pre_mon && is_suf_mon) {
        cout << "YYMM" << endl;
    } else if (is_pre_mon && is_suf_mon) {
        cout << "AMBIGUOUS" << endl;
    } else {
        cout << "NA" << endl;
    }
    
    return 0;
}