#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;

void replace_all(string& s, const string& src, const string& tgt) {
    size_t pos = 0;
    while((pos = s.find(src, pos)) != string::npos) {
        s.replace(pos, src.length(), tgt);
        pos += tgt.length();
    }
}

int main() {

    string s;
    cin >> s;
    replace_all(s, "eraser", "");
    replace_all(s, "erase", "");
    replace_all(s, "dreamer", "");
    replace_all(s, "dream", "");

    if (s == "") {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}