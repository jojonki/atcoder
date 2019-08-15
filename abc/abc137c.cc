#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<string> S;
    while (N--) {
        string s;
        vector<char> s_vec;
        cin >> s;
        for (int i=0; i<s.size(); i++) {
            s_vec.push_back(s[i]);
        }
        sort(s_vec.begin(), s_vec.end());
        s = "";
        for (int i=0; i<s_vec.size(); i++) {
            s += s_vec[i];
        }
        S.push_back(s);
    }

    sort(S.begin(), S.end());
    // for (int i=0; i<S.size(); i++) {
    //     cout << S[i] << endl;
    // }
    long int count = 0;
    long int groupCount = 1;
    string tmp = S[0];
    for (int i=1; i<S.size(); i++) {
        if (tmp == S[i]) {
            groupCount++;
        } else {
            count += groupCount * (groupCount-1) / 2;
            groupCount = 1;
        }
        tmp = S[i];
    }
    count += groupCount * (groupCount-1) / 2;

    cout << count << endl;

    return 0;
}
