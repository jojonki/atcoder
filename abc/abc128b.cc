#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    pair<pair<string, int>, int> data[100];

    for (int i=0; i<N; i++) {
        string s;
        int p;
        cin >> s;
        cin >> p;
        data[i] = make_pair(make_pair(s, -p), i+1);
    }

    sort(data, data+N);
    for (int i=0; i<N; i++) {
        cout << data[i].second << endl;
    }

    return 0;
}

int main2() { 
    int N;
    cin >> N;
    vector<string> S;
    vector<int> P;
    map<string, vector<int>> dic;
    map<string, int> idx;

    for (int i=0; i<N; i++) {
        string s;
        int p;
        cin >> s;
        cin >> p;
        dic[s].push_back(p);
        if (find(S.begin(), S.end(), s) == S.end()) {
            S.push_back(s);
        }
        idx[s+to_string(p)] = i + 1;
    }
    sort(S.begin(), S.end());

    for (int i=0; i<S.size(); i++) {
        sort(dic[S[i]].begin(), dic[S[i]].end(), greater<int>());
        for (int j=0; j<dic[S[i]].size(); j++) {
            int pt = dic[S[i]][j];
            cout << idx[S[i]+to_string(pt)] << endl;
        }

    }
    
    return 0;
}